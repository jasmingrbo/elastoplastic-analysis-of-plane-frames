function [mnpulks, pmnpulks, sulks] = o_pmnpulks_i_sulks(gvnp)
%% SECTION TITLE
% DESCRIPTIVE TEXT

    % Ova funkcija vadi èvorna pomjeranja i raèuna èvorne sile elemenata 
    
    % Definisanje globalnih varijabli
    global be bsskpe zglob
    
    % Inicijalizacija nulte matrice sila u lokalnom 
    % koordinatnom sistemu
    sulks = zeros(be, bsskpe);  
    
    % Inicijalizacija nulte matrice vektora nepoznatih 
    % pomjeranja u globalnom koordinatnom sistemu
    mnpugks = zeros(be, bsskpe); 
                                 
    % Inicijalizacija nulte matrice vektora nepoznatih 
    % pomjeranja  u lokalnom koordinatnom sistemu                             
    mnpulks = zeros(be, bsskpe); 
                                 
    % Petlja za proraèun èvornih sila elementa     
    for i=1:be
        
        % Pozivanje funkcije za formiranje matrica krutosti
        % elementa u lokalnom koordinatnom sistemu
        mkeulks = o_mkeulks(i);   
        
        % Pozivanje funkcije za formiranje matrice
        % transformacije elementa
        mt = o_mt(i);    
        
        % Proraèun matrice krutosti elementa u 
        % globalnom koordinatnom sistemu                          
        mkeugks = mt * mkeulks * mt';  
        
        % Pozivanje funkcije za formiranje lokacijskog
        % vektora elementa                               
        lv = o_lv(i);             
        
        % Petlja za formiranje matrice nepoznatih pomjeranja u globalnom
        % koordinatnom sistemu
        for j=1:bsskpe
            if lv(j) ~= 0
                mnpugks(i, j) = gvnp(lv(j));
            end
        end
        
        % Vektor cvornih sila elementa u globalnom koordinatnom sistemu
        vcseugks = mkeugks * mnpugks(i, :)';   
        
        % Vektor èvornih sila u lokalnom koordinatnom sistemu
        vcseulks = mt' * vcseugks;  
        
        % Matrica sila u lokalnom koordinatnom sistemu
        sulks(i, :) = vcseulks;     
        
        % Petlja za zaokruživanje vrijednosti matrice sulks
        for a=1:be
            for b=1:bsskpe
                if abs(sulks(a,b)) <= 0.01
                    sulks(a,b) = 0;
                end
            end
        end 
        
        % Matrica nepoznatih pomjeranja u lokalnom koordinatnom sistemu
        mnpulks(i,:) = mt' * mnpugks(i,:)';
    end
    %% SECTION TITLE
    % DESCRIPTIVE TEXT
    
    % Inicijalizacija popravljenog vektora nepoznatih pomjeranja elementa
    pmnpulks = mnpulks;   
    
    % Petlja za proraèun uglova zaokreta kondenzovanih matrica krutosti
    % elemenata
    for i1=1:be
        for j1=1:2
            if zglob(i1, j1) == 0
                Le = o_L(i1);
                if j1 == 1
                    pmnpulks(i1, j1^2+2) = -((1.5*mnpulks(i1, 2))/Le) + ((1.5*mnpulks(i1, 5))/Le) - 0.5*mnpulks(i1, 6);
                elseif j1 == 2
                    pmnpulks(i1, j1^2+2) = -((1.5*mnpulks(i1, 2))/Le) + ((1.5*mnpulks(i1, 5))/Le) - 0.5*mnpulks(i1, 3);
                end
            end
        end
    end
    
    %% SECTION TITLE
    % DESCRIPTIVE TEXT
    
end


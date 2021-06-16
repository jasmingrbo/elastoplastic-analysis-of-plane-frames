function [gmks, gvs] = o_gmks_i_gvs()

    
    % Ova funkcija formira globalnu matricu krutosti sistema i globalni vektor sila sistema
    
    % Definisanje globalni varijabli
    
    global be bssk
    
    % Asembliranje globalnog vektora sila
    
    gvs = zeros(bssk, 1);   % Inicijalizacija nultog globalnog vektora sila
    gvs = o_gvsoonc(gvs);   % Pozivanje funkcije koja asemblira globalni vektor sila
    
    % Asembliranje globalne matrice krutosti sistema
    gmks = zeros(bssk);   % Inicijalizacija nulte globalne matrice krutosti sistema
    for i=1:be
        mkeulks = o_mkeulks(i);   % Pozivanje funkcije za formiranje matrice krutosti elementa 
                                  % u lookalnog koordinatnom sistemu
        mt = o_mt(i);             % Pozivanje funkcije koja formira matrice transformacije 
                                  % elementa 
        mkeugks = mt * mkeulks * mt';   % Formiranje matrice krutosti elementa u globalnom 
                                        % koordinatnom sistemu
        lv = o_lv(i);                   % Pozivanje funckije za formiranje lokacijskog vektora 
                                        % elementa 
        
        gmks = o_gmks(gmks, mkeugks, lv);   % Pozivanje funkcije za asembliranje globalne  
                                            % matrice krutosti sistema
    end 
end


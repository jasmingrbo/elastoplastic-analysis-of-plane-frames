function [L] = o_L(i)

    % Ova funkcija raèuna dužinu elementa i
    
    % Definisanje globalnih varijabli
    
    global kc pe 
    
    % Vaðenje èvorova elementa i
    
    c1 = pe(i, 1);   % Prvi èvor elementa i
    c2 = pe(i, 2);   % Prvi èvor elementa 2
    
    % Vaðenje koordinata X i Y èvora 1 i 2
    
    x1 = kc(c1, 1); y1 = kc(c1, 2);    % Koordinate X i Y èvora 1
    x2 = kc(c2, 1); y2 = kc(c2, 2);    % Koordinate X i Y èvora 2

    L = sqrt((x2-x1)^2 + (y2-y1)^2);   % Proraèun dužine elementa i
    
end


function [mt] = o_mt(i)
%% $%^SECTION TITLE
% DESCRIPTIVE TEXT$%^
    
    % Ova funkcija formira matricu transformacije iz lokalnih u globalne koordinate
    
    % Definisanje globalnih varijabli
    
    global kc pe
    
    % Vağenje èvorova elementa i
    
    c1 = pe(i, 1);
    c2 = pe(i, 2);
    
    % Vağenje koordinata X i Y èvora 1 i 2
    
    x1 = kc(c1, 1); y1 = kc(c1, 2);
    x2 = kc(c2, 1); y2 = kc(c2, 2);
    %% SECTION TITLE
    % DESCRIPTIVE TEXT

    % Proraèun ugla koji element i zatvara sa globalnom X osom
    
    if (x2-x1) == 0
        if (y2>y1)
            alfa = 2 * atan(1);
        else
            alfa = -2 * atan(1);
        end
    elseif (x2-x1) < 0
        if (y2-y1) == 0
            alfa = 4 * atan(1);
        elseif (y2<y1)
            alfa = (4*atan(1) + atan((y1-y2)/(x1-x2)));
        end
    else
        alfa = atan((y2-y1)/(x2-x1));
    end
    %% SECTION TITLE
    % DESCRIPTIVE TEXT
    
    % Formiranje matrice transformacije
    
    mt = [cos(alfa), -sin(alfa),   0,        0,          0,      0;
          sin(alfa),  cos(alfa),   0,        0,          0,      0;
               0,           0,     1,        0,          0,      0;
               0,           0,     0,   cos(alfa), -sin(alfa),   0;
               0,           0,     0,   sin(alfa),  cos(alfa),   0;
               0,           0,     0,        0,           0,     1];
           %% SECTION TITLE
           % DESCRIPTIVE TEXT
 
end


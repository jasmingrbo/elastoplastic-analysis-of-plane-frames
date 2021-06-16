function [lv] = o_lv(i)
%% $%^SECTION TITLE
% DESCRIPTIVE TEXT$%^
    
    % Ova funkcija formira lokacijski vektor elementa i
    
    % Definisanje globalnih varijabli
    
    global pe ru
    
    % Vaðenje èvorova elementa i
    
    c1 = pe(i, 1);
    c2 = pe(i, 2);
    
    % Formiranje lokacijskog vektora iz stepeni slobode elementa i
    
    lv = [ru(c1, 1);
          ru(c1, 2);
          ru(c1, 3);
          ru(c2, 1);
          ru(c2, 2);
          ru(c2, 3)];
     %% SECTION TITLE
     % DESCRIPTIVE TEXT

end
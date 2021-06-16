function [gmks] = o_gmks(gmks, mkeugks, lv)

    
    % Ova funkcija asemblira globalnu matricu krutosti
    
    % Definisanje globalnih varijabli
    
    global bsskpe 
    
    % Petlja za asembliranje globalne matrice krutosti sistema
    
    for i = 1:bsskpe
        if lv(i) ~= 0
            for j = 1:bsskpe
                if lv(j) ~= 0
                    gmks(lv(i), lv(j)) = gmks(lv(i), lv(j)) + mkeugks(i, j);
                end
            end
        end
    end
    

end

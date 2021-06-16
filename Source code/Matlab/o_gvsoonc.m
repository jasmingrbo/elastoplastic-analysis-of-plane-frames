function [gvs] = o_gvsoonc(gvs)
%% $%^SECTION TITLE
% DESCRIPTIVE TEXT$%^
    
    % Ova funkcija formira globalni vektor sila od optereæenja na èvorovima
    
    % Definisanje globalnih varijabli
    
    global bc bsskpc ru optnc
    
    % Petlja za asembliranje globalnog vektora sila
    for i=1:bc
        for j=1:bsskpc
            if ru(i, j) ~= 0
                gvs(ru(i, j)) = optnc(i, j);
            end
        end
    end
    %% SECTION TITLE
    % DESCRIPTIVE TEXT
    
end
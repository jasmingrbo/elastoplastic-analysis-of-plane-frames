% Èisti varijable i ekran
clear
clc

% Format ispisa numerièkih varijabli
format short g

% Definisanje globalnih varijabli
global ite lambdam lambdau zglob pru czd

% Uèitavanje ulaznih podataka
up_40_2;

% Otvaranje fajla za ispis
fid = fopen('o_rp_1.txt', 'w');

% Ispis ulaznih podataka
o_iup

% Pozivanje funkcije za formiranje globalne matrice krutosti sistema i
% globalnog vektora sila
[gmks, gvs] = o_gmks_i_gvs();

% Inicijalizacija poèetnih varijabli potrebnih za petlju koja proraèunava
% faktor graniènog optereæenja

cm = zeros(be, 2);     % Èvorni momenti
lambdau = 0;           % Ukupni faktor optereæenja
rgmks = bssk;          % Rank globalne matrice krutosti sistema
lambdam = 0;           % Minimalni faktor optereæenja i-te iteracije
ite = 0;               % Broj iteracije
pmnpulksu = zeros(be,6);   % Ukupna popravljena matrica nepoznatih pomjeranja lks
cntm = zeros(be,6);        % Ukupna matrica èvornih sila 

% Petlja za proraèun faktora graniènog optereæenja
while rgmks >= bssk
    
    % Dodavanje iteracije
    ite = ite + 1;
    
    % Rješavanje sistema K * u = F
    gvnp = gmks\gvs;                     
    
    % Pozivanje funkcije za proraèun popravljenog vektora nepoznatih
    % pomjeranja elementa i vektora èvornih sila u lokalnom koordinatnom
    % sistemu
    [mnpulks, pmnpulks, sulks] = o_pmnpulks_i_sulks(gvnp);    

    % Formiranje nulte matrice faktora optereæenja
    lambda = zeros(be,2);    
    
    % Formiranje nulte matrice èvornih momenata i-te iteracije
    cmi = zeros(be, 2);    
    
    % Formiranje nulte matrice ostatka èvornog momenta
    ocm = zeros(be, 2);
    
    % Petlja za proraèun matrice faktora optereæenja 
    for c=1:be
        for d=1:2
            cmi(c, d) = sulks(c, d^2 + 2);
            if cmi(c,d) > 0 && cm(c,d) > 0 || cmi(c,d) < 0 && cm(c,d) < 0
                ocm(c,d) = mp(c,d) - abs(cm(c,d));
            elseif cmi(c,d) > 0 && cm(c,d) < 0 || cmi(c,d) < 0 && cm(c,d) > 0
                ocm(c,d) = mp(c,d) + abs(cm(c,d));
            elseif cmi(c,d) == 0 && cm(c,d) == 0
                if pru(c,3) == 1 || pru(c,3) == 0
                    ocm(c,d) = mp(c,d);
                else
                    ocm(c,d) = 0;
                end
            elseif cmi(c,d) == 0 && cm(c,d) ~= 0
                ocm(c,d) = mp(c,d) - abs(cm(c,d));
            elseif cm(c,d) == 0 && cmi(c,d) ~= 0
                if ite == 1 
                    ocm(c,d) = mp(c,d);
                elseif ite ~= 1
                    ocm(c,d) = mp(c,d) - abs(cmi(c,d));
                end
            end
            if ocm(c, d) < 0.00001
                ocm(c, d) = 0;
            end
            lambda(c, d) = ocm(c, d)/abs(cmi(c, d));
            if lambda(c, d) == -Inf
                lambda(c,d) = Inf;
            end
        end
    end
    
    % Odreðivanje minimalnog faktora optereæenja i-te iteracije
    lambdam = min(min(lambda));
    if lambdam == Inf
        break
    elseif isnan(lambda)
        disp('Formirana je rešetka, nema više èvorova u kojima može doæi do poveæanja momenta.');
        break
    end
    
    % Sabiranje matrica "cm", "pmnpulks" i "cntm" kako bi se dobile akumulirane
    % vrijednosti istih matrica zakljuèno sa i-tom iteracijom
    cm = cm + lambdam * cmi;
    pmnpulksu = pmnpulksu + lambdam * pmnpulks;    
    cntm = cntm + lambdam * sulks;
    
    % Sabiranje lambdi
    lambdau = lambdau + lambdam;
    
    % Petlja za promjenu rubnih uslova
    for e=1:be
        for f=1:2
            if round(lambda(e, f), 10) == round(min(min(lambda)), 10)
                if (pru(pe(e, f), 3)) == 1
                    zglob(e, f) = 0;
                elseif (pru(pe(e, f), 3)) == 0
                    pru(pe(e, f), 3) = 1;
                end
            end
        end
    end
    
    % Brojanje pojave èvora u matrici "pe"
    bpc = zeros(bc,1);   % Broj pojave èvora
    for h=1:be
        for k=1:2
            for l=1:bc
                if pe(h,k) == l
                    bpc(l,1) = bpc(l) + 1;
                end
            end
        end
    end
    
    % Popravljanje matrice "zglob" tj. ne dopušta n zglobova u èvoru sa n
    % elemenata, broj zglobova treba da je max n-1 inaèe globalna matrica
    % krutosti postaje singularna
    for tt=1:bc
        [rr, cc] = find(pe == tt);  % Položaj tt-og èvora
        pzglob = zeros(bpc(tt), 1); % Inicijalizacija nultog vektora pojave zgloba
        if bpc(tt) > 1
            for ttt=1:bpc(tt)
                pzglob(ttt, 1) = zglob(rr(ttt), cc(ttt));
            end
            bpn = 0;  % Broj pojave nula
            for ss=1:bpc(tt)
                if pzglob(ss) == 0
                    bpn = bpn + 1;
                end
            end
            if bpn > (bpc(tt)-1)
                zglob(rr(ttt), cc(ttt)) = 1;
            end
        end
    end

    % Petlja za novo brojanje slobodnih stepeni slobode kretanja
    bssk = 0; % Resetovanje broja stepeni slobode kretanja
    ru = zeros(bc, bsskpc); % Resetovanje matrice rubni uslovi
    for m=1:bc
        for n=1:bsskpc
            if pru(m, n) ~= 0
                bssk = bssk + 1;
                ru(m, n) = bssk;
            end
        end
    end
    
    % Petlja za fomiranje vektora faktora optereæenja i željenog
    % pomjeranja za svaku iteraciju kako bi se formirao dijagram lambda-u
    for ci=1:be
        for cj=1:6
            if czd(ci, cj) == 1;
                mt = o_mt(ci);
                lak(ite, 1) = lambdau;
                pmnpugks = mt * pmnpulksu(ci, :)'; % Prebacivanje u gks
                pomj(ite, 1) = pmnpugks(cj) * 1000;
            end
        end
    end
    
    % Ispis rezultata i-te iteracije
    o_irp
    
    % Formiranje nove globalne matrice krutosti sistema i globalnog vektora
    % novog sistema 
    [gmks, gvs] = o_gmks_i_gvs(); 
    
    % Proraèun ranka nove globalne matrice krutosti sistema za provjeru
    % while petlje
    rgmks = rank(gmks); 
end

% Zatvara otvoreni fajl za ispis
fclose(fid);    

% Ispis teksta na konzoli
disp('Izvršavam: proracun_pz_tpr.m');  
disp('Rezultati ispisani u fajlu: o_rp_1.txt');  

% {Plotanje dijagrama lambda - delta
lak =[0;lak];
round(lak, 3);
pomj = [0;pomj];
pomj = abs(pomj);
round(pomj, 3);
plot(pomj, lak, 'k-o','LineWidth', 1.5, 'MarkerFaceColor','g', 'MarkerEdgeColor', 'k', 'MarkerSize', 3)
xlabel('Ux2 [mm]', 'FontSize', 10)
ylabel('Faktor optereæenja [kN]', 'FontSize', 10)
set(gca,'FontSize', 10);

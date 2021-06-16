% Format prikaza numerièkih varijabli

format short g

% Definisanje globalnih varijabli

global be ite lambdam lambdau

% Ispis faktora graniènog opteeæenja i mjesta formiranja plastiènog zgloba

fprintf(fid, '--------------------------------------------------------------------------------------\r\n');
fprintf(fid, '                                       KORAK %g\r\n', ite);
fprintf(fid, '--------------------------------------------------------------------------------------\r\n');

fprintf(fid, 'Faktor optereæenja: L%g = %0.3f\r\n', ite,  lambdam);
fprintf(fid, 'Ukupni faktor optereæenja: L = %0.3f\r\n', lambdau);

for i=1:be
    for j=1:2
        if round(lambda(i, j), 10) == round(lambdam, 10)
            if j == 1
                fprintf(fid, 'Mjesto plastiènog zgloba: Prvi èvor elementa %g.\r\n', i);
            elseif j == 2
                fprintf(fid, 'Mjesto plastiènog zgloba: Drugi èvor elementa %g.\r\n', i);
            end
        end
    end
end
fprintf(fid, '--------------------------------------------------------------------------------------\r\n');

% Ispis ukupnog vektora nepoznatih pomjeranja elementa

fprintf(fid, '--------------------------------------------------------------------------------------\r\n');
fprintf(fid, '%49s\r\n', 'Pomjeranja èvorova');
fprintf(fid, '--------------------------------------------------------------------------------------\r\n');
fprintf(fid, '%8s %12s %12s %12s %12s %11s %12s\r\n', 'Element', 'X1[mm]', 'Y1[mm]', 'Fi1[rad]', 'X2[mm]', 'Y2[mm]', 'Fi2[rad]');
fprintf(fid, '--------------------------------------------------------------------------------------\r\n');
for i = 1:be
    fprintf(fid, '%5g %14.2f %12.2f %12.5f %12.2f%12.2f %12.5f\r\n', i, pmnpulksu(i, 1)*1000, pmnpulksu(i, 2)*1000, pmnpulksu(i, 3), pmnpulksu(i, 4)*1000, pmnpulksu(i, 5)*1000, pmnpulksu(i, 6));
end
            
% Ispis ukupnih èvornih sila na elementu

fprintf(fid, '--------------------------------------------------------------------------------------\r\n');
fprintf(fid, '--------------------------------------------------------------------------------------\r\n');
fprintf(fid, '%51s\r\n', 'Sile u elementima');
fprintf(fid, '--------------------------------------------------------------------------------------\r\n');
fprintf(fid, '%8s %12s %12s %12s %12s %11s %12s\r\n', 'Element', 'Fx1[kN]', 'Fy1[kN]', 'M1[kNm]', 'Fx2[kN]', 'Fy2[kN]', 'M2[kNm]');
fprintf(fid, '--------------------------------------------------------------------------------------\r\n');
for i=1:be
    fprintf(fid, '%5g %14.2f %12.2f %12.2f %12.2f%12.2f %12.2f\r\n', i, cntm(i,1), cntm(i,2), cntm(i,3), cntm(i,4), cntm(i,5), cntm(i,6));
end
fprintf(fid, '--------------------------------------------------------------------------------------\r\n');   
        

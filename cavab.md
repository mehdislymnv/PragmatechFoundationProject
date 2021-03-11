  
- Translator ve assebler nədir? Compiler və interpreter ilə aralarındakı fərqlər nələrdir?
    - Translator 
        - Mənbə kodunu obyektə və ya ara koda çevirmək üçün istifadə olunan xususi  proqramdir.Burda obyekt modulu və ya obyekt faylı deyilen və kompüter prosessorunun başa düşdüyü 1 və 0-larda cevirir.Bundan başqa tərs translatorlarda var, hansıki maşın kodunu istifadəçilərin başa düşə biləcəkləri program koduna çevirirlər.
      
    -  Assebler
        - Assembler aşağı səviyyəli proqramlaşdırma dilidir. Çünki o, bir əmri mnemonika adlanan simvol işarəmələrinin köməyilə ədədlər şəklində yox, maşın kodları şəklində verir. Assemblerin köməyilə çox səmərəli və kompakt proqramlar yaratmaq mümkündür. Assemblerdən adətən, sistem əlavələrin, drayver-proqramların, kompyuterin aparat resurslarına müraciət edən proqram modullarının hazırlanması üçün istifadə olunur. Aşağı səviyyəli proqramlaşdırma dillərindən, adətən yüksək səviyyəli peşəkar proqramçılar istifadə edir. Bu dillərdə tutulan proqramlar yaddaşda az yer tutmaqla yanaşı, daha sürətlə icra olunurlar. Yüksək səviyyəli proqramlaşdırma dilləri isə adi dilə daha yaxın və insan üçün daha aydın başa düşüləndir. Çox yayılmış, bəzi proqramlaşdırma dilləri haqqında məlumat verək.
        Proqramlaşdırma dilləri iki hissəyə bölünür: 
            Aşağı səviyyəli dillər (Assembler, Avtokod və s.), 
            Yüksək səviyyəli dillər (Fortran, Alqol, Kobol, Basic, Pascal, Ci və s.).
                Aşağı səviyyəli proqramlaşdırma dillərində hər operatora bir maşın əmri uyğun gəlir. Bu dildə yazılan proqram az yer tutur və tez yerinə yetirilir. Aşağı səviyyəli dillərdən sistem proqramçılar istifadə edir. Yuxarı səviyyəli proqramlaşdırma dillərində hər operator bir neçə maşın əmri ilə əvəz edilə bilər, bu isə yaddaşda çox yer tutur. 
                Yüksək səviyyəli dillərdən isə tətbiqi proqramçılar istifadə edir.
        - Compiler vs interpreter
            Compiler bir programı bütün olarak alır ve çevirirken; Interpreter programı setır setır çevirir.
            Compiler, ara kod veya hedef kodu yardar amma Interpreter herhangi bir ara kod yaradmaz. Bundan dolayisiyla Compiler, kodun oluşturulması ucun daha cox memory lazimdir.
            Compiler’da, bir segv olanda, translator  durar ve xeta duzeldikden  sonra bütün program yeniden çeviri işlemine tabe tutulur. Interpreter, bunun tam eksini , eğer bir xeta meydana geldiyinde, o anki çeviriyi engeller ve xeta duzeldiyden çeviriyi qaldiqi yerden devam ettirir. Bugorede debug  daha asandir.
            Compiler’da, Interpreter’e nezeren sehv tapmaq daha cetindir.
            Compiler, C, C++, C#, Scala, TypeScript gibi dillerde isdifade ederken, Interpreter PHP, Perl, Ruby, Python kimi dillerde çalıştırılır.
            Compilation ve interpretation bir programlama dilini uygulamak için beraber kullanılabilir. Compiler intermediate level code’u ürettikten sonra masin koduna derl cevirerken, interpreter terefinden yorumlanır.
- Rəqəm və ədədlərin maşın dilinə tərcümə olunma prosesini bilirik. Bəs hərflər və simvollar necə tərcümə olunur?
    - Mətn tipli informasiyanın kodlaşdırılması üçün ASCII standartı American Standard Code for Information Interchange qəbul edilmişdir. Bu standartdan 256 müxtəlif simvolun – ingilis əlifbasının baş və kiçik hərflərinin, 0-dan 9-a qədər rəqəmlərin, durğu işarələrinin və xüsusi idarəedici simvolların təsviri zamanı istifadə edilir.
     Mətn tipli informasiyanın kodlaşdırılması üçün ASCII standartı American Standard Code for Information Interchange qəbul edilmişdir. ASCII-da 256 kod var. Hər bir kod yaddaşda 1 bayt (yəni 8 bit) yer tutur.ASCII cədvəlindən başqa digər kodlaşdırma sistemləri də mövcuddur. Bunlara misal olaraq Windows 1251, КОИ-8, UTF və s. sistemlərini göstərmək olar. Bu sistemlərdə də ASCII-da olduğu kimi 1 simvolun kodlaşdırılması üçün 8 bit və ya 1 bayt istifadə olunur.
- Günümüzdə istifadə olunan Js,PHP,Python və C# dillərində ortaq istifadə olunan data növləri hansılardır və qısaca izahatlarını yazın
    String - bu məlumat növünə mətnlər daxildir
    Boolean - bu məlumat növünün iki dəyəri var true və false

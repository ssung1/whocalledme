#!Scripts/python

import unittest
from bs4 import BeautifulSoup
import puller

class TestPuller( unittest.TestCase ):
    def setUp( self ):
        self.for_real = """
            <!DOCTYPE html>
            <!-- saved from url=(0020)http://800notes.com/ -->
            <html itemscope="" itemtype="http://schema.org/WebPage"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>Phone Number Lookup</title><meta data-b="/" data-r="//sys.octo.net/" data-a="28" data-e="48314afc52a3dea" id="oos_im" name="oos_im" content=""><meta name="description" content="Type a phone number in the box below and click &#39;Search&#39; to find out who is using that phone number."><meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1,maximum-scale=1,user-scalable=0"><meta name="theme-color" content="#a9c3e4"><meta name="format-detection" content="telephone=no"><meta name="SKYPE_TOOLBAR" content="SKYPE_TOOLBAR_PARSER_COMPATIBLE"><script>/*<![CDATA[*/window.oos={fs:[],onReady:function(f){if(f)oos.fs.push(f)}};if(!window.JSON||!document.querySelector)document.write('<script src="/~oos~/js/03/legacy.js"></scr'+'ipt>')/*]]>*/</script><link id="oos_css" type="text/css" rel="stylesheet" href="./callnotes_files/core.css"><script src="./callnotes_files/core.js"></script><script>/*<![CDATA[*/if(!oos.loadJS)new Image().src='/~sys~/logError/?noload_prx';/*]]>*/</script><link rel="stylesheet" href="./callnotes_files/02.css" media="all" onload="if(media!=&#39;all&#39;)media=&#39;all&#39;"><noscript>&lt;link type="text/css" rel="stylesheet" href="//sys.octo.net/css/async/02.css" /&gt;</noscript><script id="oos_async_js" src="./callnotes_files/en-US.js" defer=""></script><link rel="search" href="http://800notes.com/nb/search"><link rel="canonical" href="http://800notes.com/">     <style type="text/css">/* <![CDATA[ */
            .postCount {
                background: #fff095;
                border-radius: 50%;
                display: block;
                font-size: 12px;
                height: 40px;
                line-height: 40px;
                overflow: hidden;
                text-align: center;
                width: 40px;
            }
            
            .old {
                opacity: 0.7;
            }
            
            @media handheld, (max-width:799px) {
                .wideScrOnly {
                    display: none;
                }
            }
            /* ]]> */</style> <script>/*<![CDATA[*/
            oos.onReady(function() {
                if (oos.localStorage) {
                    var tsList = oos.localStorage.res.getString("tsList");
                    if (tsList) {
                        var tsInputs = oos.query("#previews input[name=thread_ts]");
            
                        for (var i = 0; i < tsInputs.length; i++) {
                            if (0 <= tsList.indexOf(":" + tsInputs[i].value + ":"))
                                oos.dom.getParent(tsInputs[i], ".oos_preview").className += " old";
                        }
                    }
                }
            
                var targetItemElm;
                oos.dom.addListener(oos.queryOne("#previews"), "contextmenu", function (ev) {
                    targetItemElm = ev.target;
                });
            
                oos.queryOne("#cmd_open").onclick = function () {
                    openThread(false);
                };
            
                oos.queryOne("#cmd_openBlank").onclick = function () {
                    openThread(true);
                };
            
                function openThread(blank) {
                    var li = oos.dom.getParent(targetItemElm, ".oos_listItem");
                    if (li) {
                        var a = oos.queryOne("a", li);
                        if (a)
                            open(a.href, blank ? "_blank" : "_self").focus();
                    }
                }
            
                oos.queryOne("#cmd_openLast").onclick = function () {
                    var li = oos.dom.getParent(targetItemElm, ".oos_listItem");
                    if (li) {
                        var lastPost = oos.queryOne("input[name=lastPost]", li);
                        if (lastPost && lastPost.value)
                            location = lastPost.value;
                    }
                };
            });
            /*]]>*/</script> <style type="text/css">
                    #homeTop,
                    #homeList1 {
                        background-color:#fcfcfc;
                        border-top:dotted 1px #ccc;
                        border-bottom:dotted 1px #ccc;
                        min-height:90px;
                        padding:16px;
                    }
                </style> <script defer="" async="" src="./callnotes_files/adsbygoogle.js"></script><script defer="" async="" src="./callnotes_files/gpt.js"></script><style id="style-1-cropbar-clipper">/* Copyright 2014 Evernote Corporation. All rights reserved. */
            .en-markup-crop-options {
                top: 18px !important;
                left: 50% !important;
                margin-left: -100px !important;
                width: 200px !important;
                border: 2px rgba(255,255,255,.38) solid !important;
                border-radius: 4px !important;
            }
            
            .en-markup-crop-options div div:first-of-type {
                margin-left: 0px !important;
            }
            </style><style type="text/css">a[name]:before,.oos_anchor:before,.oos_contlet:before{background:red;display:block;content:' ';margin-top:-65px;height:65px;visibility:none;width:0}</style><script src="./callnotes_files/pubads_impl_114.js" async=""></script></head><body class="oos_rightSidebar oos_year_2017 oos_month_4 oos_day_19 oos_hour_18 oos_weekday_3" dir="ltr"><div id="oos_page">   <div id="skin_page" class="oos_skin"> <div id="skin_main" role="main" style="min-height: 2698px;"> <div id="skin_main_content" style="padding-top: 57px; position: fixed; width: 936px; bottom: 16px;"> <div id="skin_main_header" class="fixed"><div id="skin_main_header_fixer_e"><div id="skin_main_header_fixer_i"><div id="skin_main_header_content"><div id="oos_contentToolbar" class="oos_headerMain"><div id="oos_headerMenu" class="oos_toolbar"><a class="oos_i_menu" title="Menu"><i></i></a><a class="oos_i_home" title="Homepage" href="http://800notes.com/"><i></i></a></div><div id="oos_headerActions" class="oos_toolbar"><a class="oos_i_search" title="Search"><i class="oos_hdr_btnIcon"></i></a></div><h1 title="Phone Number Lookup">Phone Number Lookup</h1></div></div></div></div></div><div id="oos_content" class="oos_a_40 oos_r_325126343260519915">   <div style="padding:16px"> <form action="http://800notes.com/nb/search" method="get" style="max-width:450px;margin:16px auto" _lpchecked="1"> <table style="width:100%;border-spacing:0 0"> <tbody><tr> <td style="padding-right:8px"> <input type="text" name="q" required="required" autocomplete="off" autofocus="autofocus" style="width:99%"> </td> <td style="width:1%"><input type="submit" value="Search"></td> </tr> </tbody></table> <div class="oos_comment">Phone number or keyword you want to search for</div> </form> </div> <div id="homeTop"><div class="oos_ad" data-type="adsense" data-client="ca-pub-1396518256676292" data-slot="3827703965" data-sizes="728x90,550x240,200x180" style="height: 90px;"><ins class="adsbygoogle" data-ad-client="ca-pub-1396518256676292" data-ad-slot="3827703965" style="height: 90px; width: 728px;"></ins></div></div> <div style="padding:16px"> <div><p style="text-align:justify;color:gray">800notes is a <strong style="color:#000">FREE REVERSE PHONE NUMBER LOOKUP</strong>
            database built by <strong style="color:#000">YOU</strong>, its users. Our strength is in our numbers - by sharing pieces 
            of information each of us has we are putting together a free and public phone number 
            directory with information no other service can provide.</p></div> <div><ul style="border-left:3px solid #af2626;list-style-type:none;overflow:hidden;padding-left:16px;text-align:justify"> <li style="margin-bottom:8px"><span style="color:#af2626;font-variant:small-caps">Find out who is calling and why:</span> Debt collectors, telemarketers, charities, 
            	    and survey companies often call without leaving a message. Lookup the number to read the previous reports of other users.</li> <li style="margin-bottom:8px"><span style="color:#af2626;font-variant:small-caps">Report telemarketing calls:</span> Make the Do Not Call list offenders notice 
            	    the problem by reporting their practices. No business wants bad publicity.</li> <li style="margin-bottom:8px"><span style="color:#af2626;font-variant:small-caps">Report phone fraud:</span> Did someone try to scam you? Reporting the number is 
            	    the fastest way to make public aware, and prevent others from falling victim to the scam.</li> <li><span style="color:#af2626;font-variant:small-caps">Check out a business:</span> Read other users' feedback about the phone number owner.</li> </ul></div> </div> <div id="homeList1"><script>/*<![CDATA[*/
            if(document.getElementById && document.getElementById("skin_main") 
            				&& document.getElementById("skin_main").clientWidth <= 740 ){
            document.write('<div id="div-gpt-ad-1492097572078-0" class="oos_ad" data-type="dfp" data-unit="/178523397/notes_top_2s" data-sizes="300x250" style="height:250px;width:300px"></div>');
            }
            else {
                document.write('<div class="oos_ad" data-type="adsense" data-client="ca-pub-1396518256676292" data-slot="9315834362" style="height:90px"></div>'); 
            }
            /*]]>*/</script><div class="oos_ad" data-type="adsense" data-client="ca-pub-1396518256676292" data-slot="9315834362" style="height:90px"><ins class="adsbygoogle" data-ad-client="ca-pub-1396518256676292" data-ad-slot="9315834362" style="height: 90px; width: 728px;"></ins></div></div> <ul id="previews" class="oos_noUserSelect oos_list oos_l4"> <li class="oos_listSectionTitle" style="padding-bottom:0">Latest posts</li> <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">2</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-844-857-5628">844-857-5628</a></h4><div class="oos_previewFooter">Valuable Info - <time datetime="2017-04-19T18:38:50Z">a few seconds ago</time><span class="wideScrOnly">
                                                | 8448575628
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-844">844 area code</a></span></span></div></div><div class="oos_previewBody">The company calling is loan me but they're just spoofing the number. I had them on me for the longest time. Get your credit fixed, its better than waiting for this stuff to come off. 408-753-0177 they don't always answer right away but they are really really good.<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="44b9eec8c=3abf10"><input type="hidden" name="lastPost" value="/-/contlet/0/18448575628/1191069646340148249"></div></li> <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">1</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-770-232-6548">770-232-6548</a></h4><div class="oos_previewFooter">MB - <time datetime="2017-04-19T18:38:35Z">a few seconds ago</time><span class="wideScrOnly">
                                                | 7702326548
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-770">770 area code</a></span></span></div></div><div class="oos_previewBody">Scammer posing as breeder for puppies! Then the owner told me that was just the adoption fee and a ship to door fee as the puppy was in Maryland with her as her husband was having cancer surgery. They never answered my questions I asked about the size of the puppies parents. AND kept stressing DO...<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="41f241114=3a8478"><input type="hidden" name="lastPost" value="/-/contlet/0/17702326548/1191069569701824712"></div></li> <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">53</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-877-662-5128">877-662-5128</a></h4><div class="oos_previewFooter">Abby - <time datetime="2017-04-19T18:38:26Z">a few seconds ago</time><span class="wideScrOnly">
                                                | 8776625128
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-877">877 area code</a></span></span></div></div><div class="oos_previewBody">A scam<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="45f2c8fe8=3a6150"><input type="hidden" name="lastPost" value="/-/contlet/0/18776625128/1191069523262490267"></div></li> <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">3</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-510-257-4110">510-257-4110</a></h4><div class="oos_previewFooter">Bonnie - <time datetime="2017-04-19T18:38:23Z">a few seconds ago</time><span class="wideScrOnly">
                                                | 5102574110
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-510">510 area code</a></span></span></div></div><div class="oos_previewBody">Calls saying calling aboit a federal case and I hung up<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="3842efe1e=3a5598"><input type="hidden" name="lastPost" value="/-/contlet/0/15102574110/1191069508901193211"></div></li> <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">2</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-602-566-9762">602-566-9762</a></h4><div class="oos_previewFooter">CV - <time datetime="2017-04-19T18:38:20Z">a few seconds ago</time><span class="wideScrOnly">
                                                | 6025669762
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-602">602 area code</a></span></span></div></div><div class="oos_previewBody">Calls from this # keep coming into our office, yet when we answer, no one responds.<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="3bb345082=3a49e0"><input type="hidden" name="lastPost" value="/-/contlet/0/16025669762/1191069491721323850"></div></li> 
            
                                                    
                                                    <!-- start number -->
                                                    <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">48</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-714-549-8179">714-549-8179</a></h4><div class="oos_previewFooter">Willie - <time datetime="2017-04-19T6:06:20Z">a few seconds ago</time><span class="wideScrOnly">
                                                    | 7145498179
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-714">714 area code</a></span></span></div></div><div class="oos_previewBody">Zisafca me pamnad gekevfiz imag ozacupkej cu bagaer cev av mow jo duzpiffob. Tachi umpilrif nopiet giwe badzevkob puvup edwit asalu wapudke rabitso co fumtep so wuwup rojwa cij. Hegergaz ico wiz fafag og ahi aketeh tughuc cocweof re buzemez fucsec comaak.<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="3bb345082=3a49e0"><input type="hidden" name="lastPost" value="/-/contlet/0/16025669762/1191069491721323850"></div></li>
                                                    <!-- end number -->
                                                    
                                                    <!-- start number -->
                                                    <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">6</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-325-457-7075">325-457-7075</a></h4><div class="oos_previewFooter">Ann - <time datetime="2017-04-19T8:53:20Z">a few seconds ago</time><span class="wideScrOnly">
                                                    | 3254577075
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-325">325 area code</a></span></span></div></div><div class="oos_previewBody">Matuca sukmowiro to cihdamvet im do hocjimor na okbisen ukle ukuvu neven du. Het hesguveka puhegdi sen le suzetak tihev ez vojefi tuk la jic ded bu du ka gibe ulewohwe. Wacji vu pufwipe fu pulmo fo ohiuh bubniep ijiodufab ken aneteraw ef. Lucagdoj vuh ir hoove fa gudpew bu eji kedic owgel bir henhal bidroc feji ekapoek ablu. Nahoti zifuci zawubaci mocfikub kipukje defelana gi ihuza pu uk neslilca vibute. Was cun pas pihpe jigirwo maew ti uhpugap nuzecep erzigi tofoelo pibtu map de azazu azdi ba ri. Fiv udica upejo rimuwkih fasepdum igopigno ta fahdag birki cijcev ak upuus si omzavu dos. 😞<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="3bb345082=3a49e0"><input type="hidden" name="lastPost" value="/-/contlet/0/16025669762/1191069491721323850"></div></li>
                                                    <!-- end number -->
                                                    
                                                    <!-- start number -->
                                                    <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">1</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-242-863-8658">242-863-8658</a></h4><div class="oos_previewFooter">Dora - <time datetime="2017-04-19T7:44:20Z">a few seconds ago</time><span class="wideScrOnly">
                                                    | 2428638658
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-242">242 area code</a></span></span></div></div><div class="oos_previewBody">Omga pap josil reflo pi nerfij igze sin ba raz ra vameg fu zuhbuh. Nivbow orto luiva arvavege dalzed gekide jafkete getahis kefilufi kol uhho ju hugi nasepud. Bot ohiim tad emvaz haivwoc lovu rucwuw cu midda sehbikti cimimfus ze niw ca inaawa acefubzam. Omace murib fah pihhoehi sipak nebnalmag muloom pano jolukanu duergu ogehi keh jud rerufas naafive ol. Adudakuj kabanke as kezejuru iszougo noc rasu gin jah ozi vuwesu zatomi kopi gep na umuuho. Ju ko rahme udeimkip dino egi gilgo urriz jef goju jef daj erjof hoaf nu viozcef toov faj.<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="3bb345082=3a49e0"><input type="hidden" name="lastPost" value="/-/contlet/0/16025669762/1191069491721323850"></div></li>
                                                    <!-- end number -->
                                                    
                                                    <!-- start number -->
                                                    <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">13</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-719-475-2667">719-475-2667</a></h4><div class="oos_previewFooter">Logan - <time datetime="2017-04-19T15:34:20Z">a few seconds ago</time><span class="wideScrOnly">
                                                    | 7194752667
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-719">719 area code</a></span></span></div></div><div class="oos_previewBody">Ibkoaj taze lu capakgin lutniwem fo vakvozus gowoore dovva siwol nuzjotlo fovuh alda zilvignen dovjo. Hij zug coh upuata lor dogijukoh ow cokor kabu luso totepha deifiab ezwagra jegubiju mev. Zera wif er te ubbagwe detihe awuokapef urelehin vawco otutac zemzepki kok oneopsi toaf osru gu lo ci. Tu hefkuhdo ca museb fiffok olvetgo ru zorfijdih pijtupe gec lorbej noar sogjuwem gowvaj huwtulal wuhdo najar. Nodmon hob ew owfegcol bavaf ug fikra sigdo mid lip rit bij zaceg gegmi vufbujol ege jocho.<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="3bb345082=3a49e0"><input type="hidden" name="lastPost" value="/-/contlet/0/16025669762/1191069491721323850"></div></li>
                                                    <!-- end number -->
                                                    
                                                    <!-- start number -->
                                                    <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">97</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-961-825-5572">961-825-5572</a></h4><div class="oos_previewFooter">Jason - <time datetime="2017-04-19T15:16:20Z">a few seconds ago</time><span class="wideScrOnly">
                                                    | 9618255572
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-961">961 area code</a></span></span></div></div><div class="oos_previewBody">Gok piblinvuc nide monbazne mizde nesbidaru fuagu adsaas towbu cuwra jiniivi widdogve mecinicun varegu beven danene ibozi pisutene. Bo mad zeloktav tuvne pugudozit ebi raw zu negambo be afaja zew aveev. Gi ikimiwka zetsibe egufen ditrovav gadecoj awzopeli wokvacuh hitmib ci wo cawwa. Puje polnetzu ke van hedvaceb vucah cofso demvatga feplo bed ektug pefocap kov awdizsom wiufho is wuspi luleza. Osifaktuv bomi jiuba uhwioro ru ed wagoh diconi wulbi zugo vepopuzu gug. Gojomba man cozzopjus dilabtig zemagbow burkun bo aju adgoel aphoew vec ratkuiv kanun lugajeduf dar low.<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="3bb345082=3a49e0"><input type="hidden" name="lastPost" value="/-/contlet/0/16025669762/1191069491721323850"></div></li>
                                                    <!-- end number -->
                                                    
                                                    <!-- start number -->
                                                    <li class="oos_listItem" contextmenu="menu_open"><div class="oos_preview oos_preview40"><div class="oos_previewSide"><span class="postCount">4</span></div><div class="oos_previewMain"><h4 class="oos_previewHeader"><a href="http://800notes.com/Phone.aspx/1-(426)-371-8225">(426)-371-8225</a></h4><div class="oos_previewFooter">Clifford - <time datetime="2017-04-19T9:25:20Z">a few seconds ago</time><span class="wideScrOnly">
                                                    | (426)3718225
            
                                                    <span>| <a href="http://800notes.com/AreaCode.aspx/1-(426)">(426) area code</a></span></span></div></div><div class="oos_previewBody">Sundickag ker vawveb pir pahi kuz votoz do upnebuz codca caullok jumi tezjohzu kewjar. Mafo ituvuw idi ce vidu va uto iwenerfat hol ipwopod joaszun cuwvovfi vu. Difu zemasih ewuaku attujuw hoija padni jiv todez fup jonozabe wip ca loafwi zurac ile donavkat ek. Rufuri si jujne fi jos wowsugne pu kapaef nodho penut komusup motisof gavze ruodoboj izna. No wiz sarmipap arojimu fumamiut furitvu gu akekazaj road bic po sanezsa kog mina ibjo lenku we. Pihwi zam webose oko wefcefdul bursiche wocoppip.<small class="oos_hidden">kdxyiun2 6s,so,ltz,fz</small></div><input type="hidden" name="thread_ts" value="3bb345082=3a49e0"><input type="hidden" name="lastPost" value="/-/contlet/0/16025669762/1191069491721323850"></div></li>
                                                    <!-- end number -->
                                                    
                                                  
                                                  
                                                  
                                                  
                                                  </ul> <div class="oos_hidden"><menu class="oos_m0" id="menu_open"><li class="oos_m1" id="cmd_open"><a><i></i>Open</a></li><li class="oos_m1" id="cmd_openBlank"><a><i></i>Open in new tab</a></li><li class="oos_m1" id="cmd_openLast"><a><i></i>Open last comment</a></li></menu></div>  <div style="padding:16px"> <div style="text-align:right;padding-top:.5em;font-size:small">
                        See also <a href="http://whocallsme.com/">whocallsme.com</a> and
                        <a href="http://complaintwire.org/complaints/phone-calls">call complaints</a> @complaintwire.org
                    </div> </div>  </div> </div> </div> <div id="skin_aside" role="complementary"> <div id="skin_aside_content_wrap"> <div id="skin_aside_content" style="position: relative; width: auto;"> <div id="skin_aside_header" role="banner"> <div class="oos_toolbar"><a class="oos_i_login" title="Sign in"><i class="oos_hdr_btnIcon"></i><span>Sign in</span></a><a class="oos_i_fontMinus" title="Decrease font size"><i class="oos_hdr_btnIcon"></i></a><a class="oos_i_fontPlus" title="Increase font size"><i class="oos_hdr_btnIcon"></i></a></div> <div id="skin_site_header"> <a id="skin_site_name" href="http://800notes.com/">800Notes</a> <div id="skin_site_slogan">Directory of UNKNOWN Callers</div> </div>  </div> <div id="skin_site_menu" role="navigation"><div class="oos_widget oos_widgetFrame"><div class="oos_widgetBody"><ul class="oos_list"><li class="oos_listItem oos_selected"><a href="http://800notes.com/">Homepage</a></li><li class="oos_listItem"><a href="http://800notes.com/forum/">Forum</a></li><li class="oos_listItem"><a href="http://800notes.com/news/">News</a></li><li class="oos_listItem"><a href="http://800notes.com/arts/">Articles</a></li><li class="oos_listItem"><a href="http://800notes.com/videos/">Videos</a></li></ul></div></div></div>  <div class="oos_widgetPanel"><div class="oos_widget oos_widgetFrame oos_widget_23"><div class="oos_widgetTitle">Search</div><div class="oos_widgetBody"><form method="get" action="http://800notes.com/nb/search.aspx" style="padding:16px"><table style="border-collapse:collapse;"> <tbody><tr> <td style="width:100%;padding-right:8px;"><input type="search" style="width:100%" name="q" required="required" placeholder="Phone number or search phrase" vcard_name="search"></td> <td><input type="submit" value="Search"></td> </tr> </tbody></table> </form></div></div><div class="oos_widget oos_widgetFrame oos_widget_75779496564982070"><div class="oos_widgetTitle">Latest Forum Threads</div><div class="oos_widgetBody"><ul class="oos_list oos_l4" style="white-space:nowrap"><li class="oos_listItem" title="Who gets fooled most by phone fraud?"><a href="http://800notes.com/forum/ta-108743db13744b3a/who-gets-fooled-most-by-phone-fraud">Who gets fooled most by phone fraud?</a><div class="oos_comment">Posts: 3 | Last post: <time datetime="2017-04-19T18:22:40Z">16 min ago</time></div></li><li class="oos_listItem" title="Weird number phoned my mobile earlier: Identified as  +10 nothing else?!"><a href="http://800notes.com/forum/ta-86b03986788c555/weird-number-phoned-my-mobile-earlier-identified-as-10-nothing-else">Weird number phoned my mobile earlier: Identified as  +10 nothing else?!</a><div class="oos_comment">Posts: 159 | Last post: <time datetime="2017-04-19T17:01:17Z">1 h 37 min ago</time></div></li><li class="oos_listItem" title="New Phone Scam Targets Your Kids"><a href="http://800notes.com/forum/ta-10875aa6e46af233/new-phone-scam-targets-your-kids">New Phone Scam Targets Your Kids</a><div class="oos_comment">Posts: 5 | Last post: <time datetime="2017-04-19T16:29:14Z">2 h 9 min ago</time></div></li><li class="oos_listItem" title="&quot; 909&quot;  area  code  fraud  scams / fake  calls and  texts"><a href="http://800notes.com/forum/ta-563248ceddbd631/909-area-code-fraud-scams-fake-calls-and-texts">" 909"  area  code  fraud  scams / fake  calls and  texts</a><div class="oos_comment">Posts: 666 | Last post: <time datetime="2017-04-19T16:20:00Z">2 h 18 min ago</time></div></li></ul></div><div class="oos_widgetFooter"><a href="http://800notes.com/forum/latest">more</a></div></div><div class="oos_widget oos_widget_40653309173496980"><div class="oos_widgetBody"><script>/*<![CDATA[*/
            if(0 <= document.getElementById("skin_aside").offsetLeft){
            document.write('<div id="div-gpt-ad-1487439942451-0" class="oos_ad" data-type="dfp" data-unit="/178523397/notes_side_300x250" data-sizes="300x250" style="width:300px; height:250px"></div>');
            }
            else {
            document.write('<div id="div-gpt-ad-1487440238680-0" class="oos_ad" data-type="dfp" data-unit="/178523397/notes_side_3s" data-sizes="300x250" style="width:300px; height:250px"></div>');
            }
            /*]]>*/</script><div id="div-gpt-ad-1487439942451-0" class="oos_ad" data-type="dfp" data-unit="/178523397/notes_side_300x250" data-sizes="300x250" style="width:300px; height:250px"></div></div></div><div class="oos_widget oos_widgetFrame oos_widget_20"><div class="oos_widgetTitle">Latest News</div><div class="oos_widgetBody"><ul class="oos_list oos_l4"><li class="oos_listItem"><a href="http://800notes.com/news/mkXd3xoXTQs/dmca-abuse-george-caceres-web-sheriff-john-e-henehan">DMCA abuse: George Caceres, Web Sheriff, John E. Henehan</a></li><li class="oos_listItem"><a href="http://800notes.com/news/M13OPHI-4Qg/marketers-of-free-ipad-settles-with-ftc">Marketers of “FREE” iPad settles with FTC</a></li><li class="oos_listItem"><a href="http://800notes.com/news/c7nmt6MeiQg/ftc-brings-first-case-alleging-text-messages-were-used-in-illegal-debt-collection-scheme">FTC Brings First Case Alleging Text Messages Were Used In Illegal Debt Collection Scheme</a></li><li class="oos_listItem"><a href="http://800notes.com/news/eMlkJ3EgaAg/ftc-gets-court-to-halt-phony-payday-loan-broker">FTC Gets Court to Halt Phony Payday Loan Broker</a></li><li class="oos_listItem"><a href="http://800notes.com/news/H253VpslPwg/celebrating-the-do-not-call&#39;s-10th-anniversary">"Celebrating" The Do Not Call's 10th Anniversary</a></li></ul></div></div><div class="oos_widget oos_widget_40647227097152629"><div class="oos_widgetBody"><script>/*<![CDATA[*/
            if(0 <= document.getElementById("skin_aside").offsetLeft)
            document.write('<div id="div-gpt-ad-1487762854620-0" class="oos_ad" data-type="dfp" data-unit="/178523397/notes_side_2" data-sizes="300x250" style="width:300px; height:250px"></div>');
            /*]]>*/</script><div id="div-gpt-ad-1487762854620-0" class="oos_ad" data-type="dfp" data-unit="/178523397/notes_side_2" data-sizes="300x250" style="width:300px; height:250px"></div></div></div><div class="oos_widget oos_widgetFrame oos_widget_21"><div class="oos_widgetTitle">Latest Articles</div><div class="oos_widgetBody"><ul class="oos_list oos_l4"><li class="oos_listItem"><a href="http://800notes.com/arts/I2neMkbUAAo/where-to-report-phone-crime">Where to Report Phone Crime</a></li><li class="oos_listItem"><a href="http://800notes.com/arts/BMoEKwOEhQA/16-ways-you-can-be-phone-scammed">16 Ways You Can be Phone Scammed</a></li><li class="oos_listItem"><a href="http://800notes.com/arts/MM8EKwmEhQA/9-things-to-do-when-your-identity-stolen">9 Things To Do When Your Identity Stolen</a></li><li class="oos_listItem"><a href="http://800notes.com/arts/Jb8EW-eDhQA/harassing-calls-from-a-debt-collector-here-is-what-you-need-to-know">Harassing calls from a debt collector? Here is what you need to know</a></li><li class="oos_listItem"><a href="http://800notes.com/arts/mM8EewmEhQA/harassing-phone-calls-what-to-do">Harassing Phone Calls: What To Do</a></li></ul></div></div></div> <div class="oos_widgetPanel"></div> <div id="skin_sidebarZone2"><script>/*<![CDATA[*/
            if(0 <= document.getElementById("skin_aside").offsetLeft){
            document.write('<div id="div-gpt-ad-1487440140240-0" class="oos_ad" data-type="dfp" data-unit="/178523397/notes_side_300x600" data-sizes="300x600" style="height:600px;width:300px"></div>');
            }
            /*]]>*/</script><div id="div-gpt-ad-1487440140240-0" class="oos_ad" data-type="dfp" data-unit="/178523397/notes_side_300x600" data-sizes="300x600" style="height:600px;width:300px"></div></div> <div id="skin_footer" role="contentinfo"><p> <a href="http://800notes.com/contactUs/">Contact Us</a>
            			| <a href="http://800notes.com/nb/privacyPolicy">Privacy Policy</a>
            			| <a href="http://800notes.com/nb/tos">Terms of Service</a>
            			| <a href="http://800notes.com/nb/legal">Legal Stuff</a> </p> <p>Copyright <a href="http://800notes.com/nb/about">800notes.com</a> 2017</p></div> </div> </div> </div> </div>  </div><div style="display:none"><ul id="oos_hdrUserMenu" class="oos_m0"><li class="oos_m5">User - </li><li class="oos_m1"><a href="http://800notes.com/~sys~/my/profile.aspx">Profile</a></li><li class="oos_m1"><a href="http://800notes.com/~sys~/my/posts.aspx">My Posts</a></li><li class="oos_m1"><a href="http://800notes.com/~sys~/my/replies.aspx">Replies to My Posts</a></li><li class="oos_m1"><a href="http://800notes.com/~sys~/login/signOut.aspx">Sign Out</a></li><li class="oos_m5">OctoNet</li><li class="oos_m1"><a href="https://my.octo.net/my/account/">Login Credentials</a></li></ul><ul id="oos_hdrSignInMenu" class="oos_m0"><li class="oos_m5">800notes.com</li><li class="oos_m1"><a href="http://800notes.com/~sys~/login/">Sign In</a></li><li class="oos_m1"><a href="http://800notes.com/~sys~/login/signUp.aspx">Register</a></li></ul></div><span id="skin_css"></span></body></html>        
            """
            
        self.list_item = """
            <li class="oos_listItem" contextmenu="menu_open">
             <div class="oos_preview oos_preview40">
              <div class="oos_previewSide">
               <span class="postCount">
                4
               </span>
              </div>
              <div class="oos_previewMain">
               <h4 class="oos_previewHeader">
                <a href="http://800notes.com/Phone.aspx/1-(426)-371-8225">
                 (426)-371-8225
                </a>
               </h4>
               <div class="oos_previewFooter">
                Clifford -
                <time datetime="2017-04-19T9:25:20Z">
                 a few seconds ago
                </time>
                <span class="wideScrOnly">
                 | (426)3718225
                 <span>
                  |
                  <a href="http://800notes.com/AreaCode.aspx/1-(426)">
                   (426) area code
                  </a>
                 </span>
                </span>
               </div>
              </div>
              <div class="oos_previewBody">
               Sundickag ker vawveb pir pahi kuz votoz do upnebuz codca caullok jumi tezjohz
            u kewjar. Mafo ituvuw idi ce vidu va uto iwenerfat hol ipwopod joaszun cuwvovfi
            vu. Difu zemasih ewuaku attujuw hoija padni jiv todez fup jonozabe wip ca loafwi
             zurac ile donavkat ek. Rufuri si jujne fi jos wowsugne pu kapaef nodho penut ko
            musup motisof gavze ruodoboj izna. No wiz sarmipap arojimu fumamiut furitvu gu a
            kekazaj road bic po sanezsa kog mina ibjo lenku we. Pihwi zam webose oko wefcefd
            ul bursiche wocoppip.
               <small class="oos_hidden">
                kdxyiun2 6s,so,ltz,fz
               </small>
              </div>
              <input name="thread_ts" type="hidden" value="3bb345082=3a49e0">
               <input name="lastPost" type="hidden" value="/-/contlet/0/16025669762/11910694
            91721323850"/>
              </input>
             </div>
            </li>
            """
    
    def test_html_parser_module( self ):
        import html.parser

    def test_html_load_single_tag( self ):
        some_html = ("<html><head><title>Title</title></head>"
            "<body><div name='some div'>hey there</div></body></html>")
        soup = BeautifulSoup( some_html, "html.parser" )
        self.assertEqual( soup.div.string, "hey there" )
        
    def test_html_load_multi_tag( self ):
        some_html = ("<html><div>pablo</div>"
            "<div>tyrone</div></html>")
        soup = BeautifulSoup( some_html, "html.parser" )
        self.assertEqual( soup.find_all( 'div' )[1].string, "tyrone" )
        
    def test_real_html_find_ul( self ):
        soup = BeautifulSoup( self.for_real, "html.parser" )
        soup.find_all( 'ul' )
        
    def test_real_html_find_ul_previews( self ):
        previews = puller.find_previews( self.for_real )
        self.assertEqual( len( previews ), 1 )
        
    def test_real_html_find_list_items( self ):
        previews = puller.find_previews( self.for_real )
        list_items = puller.find_list_items( previews[0] )

    # fix later        
    def test_list_item_find_count( self ):
        item = BeautifulSoup( self.list_item, "html.parser" )
        count = item.div.div.span.string    
        self.assertEquals( count.strip(), "4" )
            
    # fix later        
    def test_list_item_find_phone_number( self ):
        item = BeautifulSoup( self.list_item, "html.parser" )
        main_div = item.div.find_all(
            name = "div", attrs = { "class": "oos_previewMain" } )
        self.assertEquals( len( main_div ), 1 )
        self.assertEquals( main_div[0].h4.a.string.strip(),
            "(426)-371-8225" )
                
        
        
                

if __name__ == "__main__":
    unittest.main()        

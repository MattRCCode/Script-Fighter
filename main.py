"""------------------------------------------------------------------

Name:       Matthew Courchaine
Course:     CS 1430, Section 04, Spring 2025
Purpose:    This Program allows you to play the fighting game
            "Script Fighter"
Input:      User will fight against an AI using 4 commands

Output: The user will either win or lose

------------------------------------------------------------------"""
import random
import sys
import time

####################################################
##### CONSTANTS ####################################
####################################################

_HEALTH100 = """\n        ||\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588||        """
_HEALTH90 = """\n        ||\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2591||        """
_HEALTH80 = """\n        ||\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591||        """
_HEALTH70 = """\n        ||\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2591\u2591||        """
_HEALTH60 = """\n        ||\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591||        """
_HEALTH50 = """\n        ||\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591||        """
_HEALTH40 = """\n        ||\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591||        """
_HEALTH30 = """\n        ||\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591||        """
_HEALTH20 = """\n        ||\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591||        """
_HEALTH10 = """\n        ||\u2588\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591||        """
_HEALTH0 = """\n        ||\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591||        """

_HIGH_ATTACK = 30
_LOW_ATTACK = 10
_LOW_BLOCK = 20

_KENNETH_JOURNEYMAN_HP = 200

########################################################################################################################
###################################  PLAYER 1 ACTIONS   ################################################################
########################################################################################################################

_PLAYER1HB = """

                     ''                 
                   ,::;;;;'             
               ','':llol::,             
           ':cokOxdxxdxkxl'             
          ,d0000KOxddooddxdoll:         
          cxOOkOOkocclodOKK00Oo'        
         :xOkkxoc;,'';odOKOOOOd,        
         ;dkOOxc''''';odOXOxxxdc'       
         'lkOOkd::ldxk0K00kddxxd:       
          ;llodxkkO00KXX0kdlccoxo,      
              ;oxkkkOOOkdcloc'':o:      
              ':,,;''',;::cdd;';c,      
             'ox;;:  ,okkkdc;  '        
             :xo'cx, ;k0kko'            
            lOXx',o, 'd0K0l             
           oKNWKl:dc'c0NNNO;            
          c0NWWNKkddxOXWWWXd'           
         'xNWWNNKxclxOXWWWNk;           
         ;kNNNNXOc ,cdKNWWNKo,          
         :kKXXX0x;   ;kXNNXXKx;         
         ;x0KKXKx;    ,dKXKKKKd'        
         'dKKKKKOc     'oOKKKKk:        
          cOKKKKk;      'o0KKK0o'       
          cOKKKKO:       ;kKKKKk:       
          :xO0kl:,        lO0Okxl'      
          ,okkd:          ';cdxkxc'     
        ,codxxdc            cdddol;     
        ',,,;;'                         """

_PLAYER1HA = """
                                        
                                        
                                        
                                        
                                        
                                        
                                        
             ;c:,,'                     
       ,::' ;lddo:,                     
      :dkd;;codxxddddxdlcccolc,   ''    
     'oxl;,:lokO0KOxddxkkkkkkxc''loc:   
      co:';llox0KKklccc:,,:c:,   ,:,    
     ,dkdloxdx0KXKkl:,                  
     ,dkxdkOkOKKXKkc,                   
      ',;:oxkOkxdl;                     
         ;:,,;,;c;                      
        cxl':;;dkx;                     
       cko':o;;k0x,                     
      :x0Odxo:xKKk:                     
     'ckNNX0xkKNOl:                     
     :okOdkxclk0x;:;                    
    'okx:;c, ,:lolllc,                  
    'o00xo:   ;lkOxk0d'                 
    'dKK0k:    lOKKKKO:                 
    'xKKKO;    'dKKKK0o                 
     lkkkd,     cO000Oc                 
    'lxxc        :dxkxc'                
   ,ldxxc         cddolc,               
    ''',  """

_PLAYER1LA = """             
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
       ,:l:;,','                        
      cO0kol:;:,                        
      o0Oxdxxdol:                       
     'cooodxxkOK0o,                     
    ':;,,;oOKK0000x:,                   
    ':c;';lxOOkkkOkddc                  
  ,;;:llcokkkkOOOxolc,                  
 ':c:;;coodxkkxxo:'                     
   ;;,col:;;oxkkkd:'                    
     ,xKKk:';oO0NNX0Oxc,                
    'dXNWXd,',d0KXNNWNX0kxoc,           
    oXNWWNx'  :xO0KXNNNNNXXKOd:'        
   :OXNNNXd     ,:oxkkOKKKKKKkdlc:,     
   lOKKXXOc           ,cdxkkdc;coddoc'  
  ,ldOOOd:                      ,lool,  
   ',;;'                         ','    
"""

_PLAYER1LB = """
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                   ',,                  
                  ;lc:::;;'             
            ':ool:loool::;'             
         ;oxk0K00Oxddkkdodd;            
        :xOkO00KXK0kddoldOOl:ll;'       
       ;xxxxkOOk0KOdllccokxlo::c;       
       ;dddkOOkxdo:,',cocoxl;,''        
        oxdxO0Od:' ''':oclxxoc:,'       
        'lodO00kl;'',:clokXNNNKxc       
         ':cdkkkxocodkkkO0KXXNNKo       
          :dxdl:clllodkOkxkO0O0Oo       
         ,dkkkxl:'  ,lkkxxkOOkkd;       
         ,ok0KKXOc   ckkxdkOkkkl        
         'lOXNNWNO;  ckkxdxkkOk:        
         ':xXNNWWNd' ;lc:cdxkkkc        
       'ldddONWWWN0;     :ool:c;        
       cdO0kkKNNNNKc    ,cooc'          
      ,oxk0KO0KXXXO:    coodoc,         
      'cloodxk0KK0x,     ';llcc;,'      
         '''',:cc;'                     """

########################################################################################################################
###################################  PLAYER 2 ACTIONS   ################################################################
########################################################################################################################

_PLAYER2HB = """                     
                 ''                     
             ';;;;:,                    
             ,::lol:,'','               
             'lxkxdxxdxOkoc:'           
         :llodxddoodxxOK0000d,          
        'oO00KKOdolccokOOkOOxc          
        ,dOOOOKOdo;''';coxkkOx:         
       'cdxxxOKOdo;'''''cxOOkd;         
       :dxxddk00K0kdol::dkOOkl'         
      ,oxoccldk0XXK0OOkkxdoll;          
      :o:''colcdkOOkkkkxo;              
      ,c;':ddc::;,'',;,,:'              
        '  ;cdkkko, ,:;;xo'             
            'okk0k;,oxc'ox:             
             l0K0d',oo,'xXOl            
            ;ONNN0ccxd:lKWNKo           
           'dXWWWXOdodkKNWWN0c          
           ;kNWWWXOl;cxKNNWWNx'         
          ,oKNWWNKd,  cOXNNNNk;         
         ;xKXXNNXk;   ;x0XXXKk:         
        'dKKKKXKd,    ;xKXKK0x;         
        :kKKKKOo'     cOKKKKKd'         
       'o0KKK0o'      ;kKKKKOc          
       :kKKKKk;       :OKKKKOc          
      'lxkO0Oo        ,:lk0Ox:          
     'cxkxdc;'          :dkko,          
     ;lodddc            cdxxdoc,        
                         ';;,,,'        
"""

_PLAYER2HA = """





                        ''              
                     ',,:c;             
                     ,:odol; '::,       
    ''   ,clocccldxdoddxxdoc;;dkd:      
   :col''cxkkkkkkxdxkOK0Okol:,;lxo'     
    ,:,   ,:c:,,:cclokKK0xoll;':oc      
                  ,ldkKXK0xdxoldkd,     
                   cdkKXXKOkOkdxkd,     
                     ;ldxkOkxo:;,'      
                      ;c;,;,,:;         
                     ;xkd;;:'lxc        
                     ,x0k;;o:'okc       
                     :kKKx:oxdO0x:      
                    ;:lONKkx0XNNkc'     
                   ;l:;x0klcxkdOko:     
                  ,lollol:, ,c;:xko'    
                 'dkxxOkl;   :ox00o'    
                 :OKKKKOl    :k0KKd'    
                 o0KKKKd'    ;OKKKx'    
                 cO0O0Oc     ,dkkkl     
                'cxxxd:        cxxl'    
               ,cloddc         cxddl,   
                                ,'''    
"""

_PLAYER2LA = """













                        ',',;:l:,       
                        ,:;:lok0Oc      
                       :lodxxdxO0o      
                     ,o0KOkxxdoooc'     
                   :lx0000KKOo;,,;:'    
                  cdxkOkkkOOxl;';c:'    
                  ,looxOOOkkkkocll:;;,  
                    '':oxxkkxdooc;;:c:' 
                   ';:dkkkxo;;:loc,;;   
                ,cx0XXNN0Oo;':kKKx,     
           ,coxk0XNNNNXK0d,',dXWNXd'    
        ':dOKXXNNNNXXK0Ox:  'xNWWNXo    
     ,:cldkKKKKKKOkxdo:,     dXNNNXO:   
  'coddoc;cdkkxdc,           cOXXKKOl   
  ,lool,                      :dOOOdl,  
    ','                         ';;,'   """

_PLAYER2LB = """








                  ,'                    
             ';::::ll;                  
             ';::loodl:loo:'            
            ;ddodkkdxkO00K0kxo;         
       ';ll:lOOdlodkO0KXK00OkOx:        
       ;c::olxkoccldkOK0kOOkxxxx;       
        '',;lxococ,,,:odxkOOkddd;       
       ',:coxxlco:'' '':dOOOxdxo        
       cxKNNNXkolc:' ';lk00Odol'        
       oKNNXXK0Okkkoccoxkkkdc:'         
       oO0O0OkxkOkdlcllc:ldxd:          
       ;dkkOOkxxkkl   ':lxkkkd,         
        lkkkOkdxkkc   cOXKK0ko,         
        :kOkkxdxkkc  ;ONWNNXOl'         
        ckkkxdc:cl;',dNWWWNXx:'         
        ;c:loo:    ;d0NWWWNOdddl'       
          'cooc,   ckKNNNNKkk0Odc       
         ,codooc   :xOXXXK0OK0kxo,      
      ',;cclc;'    ,lx0KK0kxdoolc'      
                     ';cc:,''''                    
"""
########################################################################################################################
############################################    SPLASH SCREENS #########################################################
########################################################################################################################

def title():
    #Displays Game Title
    print("""                                                                                                                                                                                                        


                                          .'.                                                                                                                                                               
                                    . ..;lc,.              .';::,.                       ......                    .;'             .........                    ....''','.....                              
                                .:dkkO0KKd;'.           .ckKNWWWN0c.             .,lxkkkOKKXXXKOxo;.          .,,.c0k,      .',;lx0KKKKXXXK0xoc'        ..,:loxkO00XNNNNXKK0000Oxdo:'.                      
                             .:kXWMWWMMW0o:.          .l0WMMMMMMMMWXd'        .,l0NMMMMMMMMMMMMMMMWx.        .xXOONXd'  .,cxKNWWMMMMMMMMMMMMMMMXl   .,lx0XWMMMMMMMMMMMMMMMMMMMMMMXkl;'                      
                           .:OWMMMMMMMW0c.          .c0WMMMMMMMMMMMMWx.  .;coxKWMMMMMMMMMMMMMMMMMMMNx.      'kWMWWWXxl::d0NWMMMMMMMMMMMMMMMMMMMMXdcd0NMMMMMMMMMMMMMMMMWMMMMWNWMMKo'                         
                          'dKWMMMMMMWOc.           .xWMMMMMMMMMMMMMMMO.  'lOXNXKKNMMNK00OO0KXNMMMMMMX:     ,OWMMMMMNKx;:kXNNK0XMMNK00OO0KXNMMMMMMMMMMMMMMMMMMMMMMMMWNX00Okdc,;c:'                           
                        .lKNWMMMMMW0c.            .kWMMMMMMNklxNMMMMMx.   .,dO0KNWMMk'.   .'oXMMMMMMK,    ,0MMMMMMMWKc. 'o00KXWMM0;.   ..cKMMMMMMMMMMMMMMMMMMMMMMMWXo'..                                    
                       .oNMMMMMMMWx.             .xWMMMMMMNo. .kMMMMNl     .xNMMMMMWx.     ;0WMMMMMWx.   .kMMMMMMMMNo.  .oNMMMMMMK,     .xNMMMMMMWWWWWWNXNWMMMMMMMMK;                                       
                       cXMMMMMMMMO.              lNMMMMMMNl   .oNMMMO'     cNMMMMMMNl    .oXMMMMMMNx'  ..oWMMMMMMMNl.   .OMMMMMMMK,    ;OWMMMMMWKOkxl:,':ONMMMMMMMWd.                                       
                      :XMMMMMMMMMx.             ,KMMMMMMWd.    ,KMMXc     .kMMMMMMMK,  .lKWMMMMMWO;    ,xKMMMMMMMWd.    'OMMMMMMWx.  ,xNMMMMMMNd..     .lXWMMMMMWWO'                                        
                      lNMMMMMMMMMXd'            oWMMMMMMO'     :XWKc.     ,KMMMMMMWo.'oKWMMMMMW0c.     lXWMMMMMMWO.     ;KMMMMMMNc 'xXMMMMMMWk;        ,kNMMMMMMMNl                                         
                      .kWMMMMMMMMMMXo'         .kMMMMMMWo      oXx'       oWMMMMMMXdxXMMMMMMNOc.      .OMMMMMMMMK;      cNMMMMMMXdxXMMMMMMW0c.         lNMMMMMMWWk.                                         
                       .lKWMMMMMMMMMWXOc.      ,KMMMMMMX:      ';.       .OMMMMMMMWWMMMMMMXx;.        ;XMMMMMMMWd.     .dWMMMMMMWWMMMMMMNkc.          .kMMMMMMMWX:                                          
                         .ckKNMMMMMMMMMWx.     :XMMMMMMK,                cNMMMMMMMMMMMMNOl'           :XMMMMMMM0'      ,KMMMMMMMMMMMMWKd,             ,0WMMMMMMWk.                                          
                            .,o0WMMMMMMMWk.    ,KMMMMMM0'               .OMMMMMMMMMMMWO:.             :XMMMMMMWo       lNMMMMMMMMMN0x:.               lNWMMMMMN0;                                           
                               ,0MMMMMMMMXc    'OMMMMMMK,       'ol.   'xNMMMMMMMMMMMWX0xl;.          '0MMMMMW0,      'kWMMMMMMNOl,.                 .dMMMMMMMWx.                                           
                              'xNMMMMMMWNO,    .xWMMMMMNl     'dXK:   .dWMMMMMMMMMMMMMMMMMWKx:.        c0NMMMWx.      lNMMMMMMNo.                     lNMMMMMMX:                                            
                           .:xXMMMMMMWN0o'      ;KMMMMMMKc..'oXMXc     cXMMMMMMWNNWWMMMMMMMMMW0c.      .'lXMMNl       ,KMMMMMMK,                      '0MMMMWXx.                                            
                        'ckXWMMMMMMWXkc'         ,OWMMMMMWK0XWMXc      :XMMMMMWk,',:cok0KXNWWMMO'         lNMNc       '0MMMMMWd.                      .OMMWN0k:                                             
                     .:xXMWWMMMMMN0o;.            ,OWMMMMMMMMWO;       ;KMMMMM0,       .',,;oKWNo.        .OMNc       .kMMMMMX:                       .kMMN0O0c                                             
                    .xXWMMWWWN0xl,.               .cO0O0XNWXkc.        ,KMMWWNo              ,xOl.        .dWNo        :KMMMN0,                        lXWX0kd,                                             
                    .d0KKOdl:'.                     ....,:;.           'OMWxco,                .           .cxo.       .dWXdcc.                        'kN0:.                                               
                     ....                                               ,kx.                                  '.        ,Od.                           .oOc.                                                
                                                                         ..                                              ..                             .'                                                  



                                                                                                                 ..'.                                                                                       
                                                                                                             .':dOx:.                                                                                       
                                                                      ..                                   'oO0XWNk,                                                                                        
                     .';:ccclloxkOko;..                        .'coxxOKK0x,                              .oXMMWWWN0l.                                                                                       
                 ';okKNWMMMMMMMMMMMMWX0x;.       .;,.        .oONWMMMMMMMMXl.                          :xKWMMMMMWNx.               .......          .......                       ........                  
             .,cxXWWMMMMMMMMMMMMMMMMMMMMNo.  ',.'k0c.      .oKWMMMMMMMMMMMMNd.                       .dNMMMMMMMMWx.    ..',:loxxxk00KXXK00OOOkxooox0KXXXXX0Oxo;.           ..,cok0KXXK0000Okd:.             
          .',c0NNWMMMMMMMMMMMWWMWWMMMWWNWNd,c0OxKWO;     .:0WMMMMMMMMMMMMMMMK,             ;o,      'OWMMMMMMMMWx. .:okKNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd.     .'cd0XWMMMMMMMMMMMMMMMWK:            
             .;c:ckNMMMMMWNKOxdollllc:;,:cokXWNNMNOl'   .dNMMMMMMMKdloOWMMMMK;           ,dXNl     ,0WMMMMMMMMWOcckXWMMMMMMMMMMMMMMMWWMWMMMMMMMMMMMMMMMMMMMWWNNKk;   ';oKNWMMMMMMMMMMWWMMMMMMMMKc.          
                 'xNMMMMMXl.             .dXWMMMMWXk'  'OWMMMMMMMK:   .oNMMNx'         .dNMMK,    'OWMMMMMMMMMNKXWMMMMMMMMMMMMMMMMWXOO0OkkkxOWMMMMMNKOkxdllc,''.    .,o0NNXKKWMMNKK0OO0KXNMMMMMMK,          
                .kWMMMMMM0'             .dWMMMMMMMNx. ,0WMMMMMMWO,     .OWKo,.....   .:0WMMMWx.  .xWMMMMMMMMMNKXWWMMMMMMMMMMMMMMMMO;...    .xWMMMWNk'                 .:k0KKNWMWo..  ..,kWMMMMMMO.          
                cNMMMMMMM0:..           oNMMMMMMMWO' 'OMMMMMMWNk'   .,:dXWXKKKKKO:  ,xNMMMMMM0'  lNMMMMMMMMMN0xx0NMWWNXNWMMMMMMMMWo        lNMMMMWXd. ..  .'.          ,0WMMMMMNc     .cKMMMMMMNl           
               .kMMMMMMMMWWX0Okxddol:. ;KMMMMMMMWk' .kWMMMMMWXk,.;lkKNMMMMMMMWOc'  .kWMMMMMMNo..cKMMMMMMMMMWx'..lkxl:',dNMMMMMMWW0,       ;KMMMMMMMKkk00kx0N0do,      .dWMMMMMMK;    'xNMMMMMWXo.           
               cNMMMMMMMMMMMMMMWWWXx:..xWMMMMMMM0,  lNMMMMMMX0l:ONWMMMMMMMMMW0;    lXWMMMMMMWXKNWMMMMMMMMMMWX0Ox:.    ,OWMMMMMMWNl       .xWMMMMMMMMMMMMMMMMWOl.      .OMMMMMMMx.  'oXMMMMMMNx'             
              .kMMMMMMMMMMMMMMMN0l.   ;XMMMMMMMK;  ,0MMMMMMNNXKNMMMMMMMMMMMMWk'   ,ONWMMMMMMMMMMMMMMMMMMMMMMMMWk'    .oKWMMMMMMMO.       ;KMMMMMMMMMMMMMMWXOl.        ,KMMMMMMXc.,dXWMMMMMNk;               
              ,KMMMMMMMMMWN0xoc;.     oWMMMMMMWd.  oWMMMMMMK000XWMMMWMMMMMMWNk'   lXWMMMMMMMMMMMMMMMMMMMMWNNXKO;     ,0WMMMMMWWX:       .dWMMMMMMMMMMWNXx:.           lNMMMMMW0okNMMMMMMNk;.                
              lNMMMMMMXxl:'.         .xMMMMMMWO.  .kMMMMMMNKx:c0WNOxONMMMMMXO;   ;OWMMMMMMMMMMMMMMMMMMMMMNOoc:.      lNMMMMMMWWx.       'OMMMMMMMMMWNOo;.            .kWMMMMMWWWMMMMMWKd,                   
             .xWMMMMMNc              .OMMMMMMNc   ,KMMMMMMNXd''cc;ckNMMMMMWXo.   lNMMMMMMMMWWWWWWMMMMMMMMO'         .xWMMMMMWWK:        :XMMMMMMWKd:'.               oNMMMMMMMMMMMMNkc.                     
             .xMMMMMMO.              ,KMMMMMMO.   cNMMMMMMWNd. 'lONMMMMMMMXx.    'OWMMMMMMXkolkNWMMMMMMWNo          .xNMMMMMWXo.       .dWMMMMMMK;    .;:;cll,      '0MMMMMMMMMMMXx,                        
             .xMMMMMWo               .kMMMMMNl    ;KMMMMMMWNOlxXMMMMMMMMMN0c     .oKWMMMMWo   cXWMMMMMMXO;          ;KMMMMMMWK,        '0MMMMMMM0' .,dKWWWWKo.     'xWMMMMMMMMMMMNKOo:'                     
             .kMMMMMK,                lNMMMM0'    .kWMMMMMMMWWMMMMMMMMMMMNO,      :0WMMMMWo   cO0WMMMMMKd,          cNMMMMMMWx.        '0MMMMMMMXdd0NMMWWW0c.     'OMMMMMMMMMMMMMMMMMMNk;                   
             .kMMMMWd.                '0MMMMO.     oNMMMMMMMMMMMMMWNWMMMMM0'      .xWMMMMWx.  'x0NMMMMM0o'          ;KMMMMMN0:         '0MMMMMMMMMMMMMMWKo.       .dWMMMMMMWNWWMMMMMMMMMNkc.                
             .xMMMMX;                 .oNWMMO.     .lXMMMMMMMMMMNO:,kWMMMWd.       'kNMMMK;   .lOXMMMMMKk,          '0MMMNKko'         .dWMMMMMMMMMMMMNx,          oWMMMMMNo,,;cox0KXXNWMMWd.               
              ;kNMWx.                  .oKMMO.       ,xXWMMMWNOo,.  ,0MMMX;         .cONM0'    .o0NMMMMXO;          .OMMWNKOl.          'kNMMMMMMMMWKd,            oWMMMMMk.      ..,,,ckNWK:               
              .;KWO,                    .oNWk.         .:llc:'       :0WM0'           .c0k,     .,lOXWMNKc          .dWWXKOxc            .,cd0XNXOd:.             .dWMMMWX:             .:k0c               
              ..dd.                      .:oo'                        .cO0,             .,'        .,kWNXl           ,ONXo.                  .....                 cNMNxll.               ..                
                ..                          ',                          ...              ..          .:od;            ;kd'                                         .lKx.                                    
                                                                                                        .             .;.                                            ..                                     

    """)


def lose_screen():
    #Announces the player has lost
    print("""                                                                                                                                                      
                                                                                                                                                      
                 .;c.                                                                 ';.                                                             
     .oxl'      'kNNd.                                 ,:,'                         ,xKx.                               ..',,.          ..'''..       
     lXNXl    .cKMMNd.     .cdxxxdc.                 .xNWNO'                      .oNWKc.        .cxOOOxl'           ,ok0KKx;      .,lxOKNNNNX0o.     
    .OWWWO.  .dNMMWx.     ,ONNKXWMWKl.       ;do'   .kWWWMO.                     .xWMMNd.       .kNNXKNMWXd.       'dXMMMNx,      .oXWMMWWNXKOkd;     
    ,KMMMX; .xNMMWk.    .lOx:'..oNMMXc      ;0NNx. .xWMWWMk.                    .dWMMM0'       ;kkc'..cXMMNl     .lKWMMNk,        .;OMMNx,...         
    'OWMMWd'dNMMMO'    .kWW0,   '0MMMx.    .kWMMk. lNMMMMWd                     ;XMMMX:      .oXWK;   .OMMM0'   .oNMMMNo.          lNMMWx:ccll;.      
    .oXWMMX0NMMMK;     lNMMk.   ;KMMMO.    lNMMWl.:XMMMMMNc                    .xWMMWd.      :XMM0'   ,0MMMK,   ;KMMMMX:          '0MMMMWWWMWKo.      
     .xXWMMMMMMX:     ,0MMNl   .oNMMWx.   'OMMMK,,0MMMMMMO'                    cXMMM0'      'OMMNl    cXMMWO'   .xWMMMMXx;.       lNMMMMMWKx:.        
      .lKWMMMMNl      oWMMNc   :KMMMXc    oWMMMkcOMMWWMMMx.                   .OMMMNc       :XMMNc   :KWMMNo.    .:xKWMMMWKl.    .dWMMWKxc'           
       .oNMMMNd.      dWMMX: .lKMMMNx.   .kMMMWOOWMW0KMMMx.                   :XMMMO.       cNMMWo  cKWMMWO'        .oXMMMMNc    'OMMM0, .:llc.       
        cNMMWx.       cNMMWx:xNMMWNk'    ,KMMMWNWMMOcOMMWl                    cXMMWk;;:c:,. ;XMMMO:dXMMMNO;          :KMMMW0;    ;XMMMKddKWNO:        
       .dWMWk.        .oXMMWWMMMWXx.     :XMMMMMMWO,,0WNK;                    .xNMMWNWMMXd. .xWMMWWWMMWNk,       .;oONMMN0o.     ;XMMMMMMMKo.         
       ,0WNk.           ;kXWWWNXk:.      'kWMMMWKo. 'kX0d.                    :0WMMMMW0d;.   .:kKNWWWXOc.      .cONMMWKx:.       .c0XXKOkl.           
       'okx'              .,;,,..         .;clc;.    ','.                    :KWMMWKd;.         .',;,'.        ,kOkdc,.            ....               
         ..                                                                  .;ldd:.                            .                                     

""")


def default_win_screen():
    #Announces the player has won
    print("""                                                                                                                                                      
                                                                                                                                                      
          ..        .,:,.                                                                                 .                               .','        
        .o0x;      'kNWK:        ..'..                     .loc;.                                        co.         ..'.       .lo.    .lOK0c        
        lXNNl     :KMMW0,     .:xKNNX0d,.         ...     cKWWWO'                        .;'            lKo.       ,dxOx.     .oKWNd.  .xNWWk.        
       ,KMWMk.  .oNMMM0,     .lKK0OONMMNx.       'xko,   :KMWWMO.                      .c0NKc.         cXNk'      ;0WWWk'    ,OWMMMXl..dWMMX;         
       ;XMMMNc .dNMMMK;    .:OKd'.  cXMMWo.     .xNWNl  ;KMMWWWx.                     .oNMMMO.  .;xc  ;KMWk.     :KMMMWx.   .xNMMMMNd.;KMMWd.         
       'OWMMMk;oNMMMX:     cXMWO.   '0MMM0'     lXWMNc 'OMMMMMWl                      :XMMMNl  :0WWd..kWMNl     'OMMMM0,   .lXWMMMMWOlkWMMK;          
        lXWMMWXNMMMNl     .kMMWd.   :XMMMK,    ;KMMMO'.xWMMMMMX:                     .OMMMMO'.oXMMM0cdNMMK;     lNMMMX:    ,OWMMMMMMNKNMMWx.          
        .oKWMMMMMMNo.    .oNMWO'   .kWMMWk.   .xWMMWd.oWMMMMMWk.                     lNMMMXl,xNMMMMXOXMMMk.    .OMMMWo    .lXWMMXKWMMMMMMX:           
         .c0WMMMMWx.      dWMWx.  .dNMMWXl    :XMMMNooNMWWWMMWd.                    'OMMMM0oOWMMMMWNNMMMXc     ;KMMMO'    .xNMMNo,kMMMMMMO.           
           lXMMMWk.      .xMMM0, .dNMMMNx.   .xMMMMKkXMMXOXMMWo                     ;XMMMMNNWMMMMMMWMMMWx.     ;KMMNl     .xNMMk. ,0MMMMWd            
          .lNMMWO'       .kMMMNdcOWMMWNk'    'OMMMMWWMMNocKMMNc                     cNMMMMMMWNKXMMMMMMWO'      '0MM0'     .dNMNl   :KMMMN:            
          'OWMWO'         :KMMMWWMMMWXd.     .kWMMMMMMNo.cKNN0'                     .xNMMMMWXo'lNMMMMNx'       .oNMk.      oWMX:    :KWM0,            
          :XWNO'           'oOXNWWNKx:.      .lXWMMWNk;  :OKOo.                       ,ldxkd,  .;oO0x:.         .oNk.      'kNO'     'okl.            
          .:xk,               .',''.          .':cc:'    .'''.                                                   .:l'       .:,                       
            .'                                                                                                     ..                                 

""")


def tie_screen():
    #Announces the contest is a tie
    print("""                                                                                                                                                      
                                         
                                             .....,,'''''..                   .,,.                    ....';:::::;'..                                 
                                    ..,;:loxkkK0OKNXKKKKKKOOOOOOOOxoc:;;;'   'kN0:.             ..':okKXNNNWMMWWWXKXKd'                               
                                .:lx0XNWWWWWMMMMMMMMMMMMMMMMMMMMMMMMNKKWWXd:l0WKo:.          .;x0XNMMMMMMMMMMMMMMMMMMWXx,.                            
                            .,oOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkd0WMX0KNMWXl..       'oOKNMMMMMMMMMMMMMMMMMMMMMMMMMNx.                           
                         .;dKNMMMMMMMMMMMMMMMMMMMMMMMMWNWMWXKKXWMMNkdONMMMWMMMWKxxc.    .lXMMMMMMMMMMMMMMMMMMMMMMWWNNXOxd:.                           
                       .c0NWWMMMMMMMMMMMMMMMMMMMMMMNXNXO0KOo:,,:cc::kXWMMMMMMMWNXx'     .o0KkONMMMMMMMMWXK0kxxxxdc;,'.                                
                       ,OXNWWWMMMMMMMMMMMMMMMMMMMWKdc;,'...       'OWMMMMMMMMMMW0d,       ...oWMMMMMMNKl...                                           
                     ,o0NWMMMMMMMMMMMMMMMMMMMMMMMMk.             .kWMMMMMMMMMMMWKc          :XMMMMMMNKO,                                              
                    'odoox0XNWWMWNXKNMMMMMMMMMMWWNl              oNMMMMMMMMMMMMXc          'OMMMMMMMNX0,  ......,;'.                                  
                        .ckOOkoc;'.cKWMMMMMMMMMWWO.             ;KMMMMMMMMMMMMXc          .dWMMMMMMMMMKdoxO0OOO0NWN0doo:.                             
                         .'..     .dKWMMMMMMMWNWXc             .kMMMMMMMMMMMMNl           '0MMMMMMMMMMMMWMMMMMMMMMMMWXd'                              
                                  :OXMMMMMMMMWWWx.             cNMMMMMMMMMMMWd.           cXMMMMMMMMMMMMMMMMMMMMMMMXl'                                
                                 'dKWMMMMMMMMWMK;             .xMMMMMMMMMMMWk.           ,KMMMMMMMMMMMMMMMMMMMMN0xl,                                  
                                 cKNMMMMMMMMWWNo              '0MMMMMMMMMMKk;            dWMMMMMMMMMMMMMMMWNKkc'.                                     
                                .xNWMMMMMMMWWW0'              :XMMMMMMMMMNo.            '0MMMMMMMMMMMMMMMXOko'                                        
                                'kNMMMMMMMMWNNo               dWMMMMMMMMMO'             ;XMMMMMMMMMMMMWXOo:.                                          
                                cXWMMMMMMMMNNO.              .xMMMMMMMMMNc              cNMMMMMMMMMXxl,.                                              
                                cXWMMMMMMMNXXl               .xMMMMMMMMMO.             .xMMMMMMMMMNl       .','';::c;.                                
                               .dNWMMMMMMMWNO.               .xMMMMMMMWNl              .xMMMMMMMMMNc     'l0NNXXWWXx;                                 
                               '0MMMMMMMMMMNl                .dWMMMMMMXk,              .xMMMMMMMMMNc  .;xNMMMMMWWNd.                                  
                               '0MMMMMMMMMM0'                 :XMMMMMMMk.              .OMMMMMMMWNNxcxXWMMMMMWNNO:.                                   
                               .kMMMMMMMMWNd                  .kMMMMMMNl               ;XMMMMMMMMWWWMMMMMMMMWX0o.                                     
                                lWMMMMMMXOk;                   ;XMMMMMX:               ,KMMMMMMMMMMMMMMMMMMMNd'                                       
                                lWMMMMNXd:d,                   .oKNMMMX:                lXMMMMMMMMMMMMMMMMXx;                                         
                                :XMMMWKKK0x.                    .cOWMMX:                 lNMMMMMMMMMMMMW0o'                                           
                                .xXNN0KN00o                       :XMMN:                 .,lkKWMMMMMN0x;.                                             
                                 cXNNkxl.''                        cKKKd.                    .;cccc:'.                                                
                                 :KWW0;.                            ,;ld'                                                                             
                                 .dKOl.                                ,'                                                                             
                                  'l,                                                                                                                 
  
""")

def perfect_screen():
    #Announces eihter the player or Ai won without taking damage
    print("""                                                                                                                                                      
                                                                                                                                                      
                                                      ..,;::;'                                                         .:'     .;,.                   
       ..',;cool:.    .';coool:.     ..;cloodl;.  .cdkKNWMMMWXk;..,:lodol;.      .;odd:.     .';:clooollc;.          ,d0K:   'o00;    .;c:,.          
     .ckKNNNNWWMWk. .lONWWWNXKO:.  'oOXWWNNWMMNd..,lOWMW0xdolcldx0NMWNNXKk;.    ,kWMMMWk. .cxKNWWMMWWNXK0d'         .OMMWd.,xXWK:   .l0XXNW0l.        
     .l0NW0:':OWMN: .:0MNx;,'..    'xXWNd,,oXMM0'  'OWMK;      .lXMNd;,'.      cXMWOkXMK;,kWMWWMMMNx;'...          .dWMW0oxXWKo.   ,xOl'.lXMNl        
      :XMMx..lXMNx.  cXMW0xxkx:.   .kMMK; ;OWWK:   oWMMN0xdl,. .dWMNOxkkd;    :XMWk..xWd..;ccoKMMMO'               oNMMWXNW0l.    ,KMK;  '0MMk.       
      oWMWkl0WWO:.  ,0MMMMWKx:.    ;XMM0okNWKo.   '0MMMWX0x:.  :XMMMMWKd:.   .kMM0, .ox.     cXMMNc               ,KMMMMNOc.     .xWWk.  cXMMO.       
     .kMMMWWNk;.    oWMMXxc.      .xWMMWWNOc.     :NMWx;..    .xMMWKd:.      ,KMMx.  ..     .kMMWx.               oWMMMMXd;'.    ;KMWd  ,0WMNo        
     :XMMNkl'      .kMMXc.:ddc.   cXMMMMWOc.      ;XM0'       '0MMK:'cdd:.   ,0MWd.  ..     '0MMX:                dWMMMMMMWN0d'  ;XMWd.;0WMWk.        
    .dWMNl         .kMMWKKWKl.   .kMMWXKNWWKd'    .OWo        '0MMNKXN0c.    .xWM0;'lx,     ,KMWx.                dWMWKdooooxKO' 'OMMXOXMMNk'         
     cNM0,          :0NWN0o'     .xWWx..';coOd.   .k0,        .lKNWNOl.       ,OWWNXO;      '0WK:                 cXWK:      .;.  ,xKNWWNOl.          
     'kO:.           .','.        lOo'      ..     ,;           .','.          .,::,.        cx:.                  ,xd.             .',,'.            
      ..                           .                                                          .                      .                                

""")

def great_screen():
    #Announces the player won by a slim (10 hp) margin
    print("""                                                                                                                                                      
                                                                                       .'.                                           
                       .cxO0Oxc.                                                                      ;k0k;                                           
                    .;xXWMMMMMWO,              ..,,,,,,,'.              .,;::::;'.                  .oXMWx.           ..'',;;::;,''...                
                   ,OWMMMMMMMMMM0'        .,cxOKNWWWWWWWNXk,      .,cdk0XWWWMMWWN0o,               ,OWMMNc      .':oxk0XNNWWNNNNNNNX0xc'.             
                 .lXMMMMNOdxXMMMX;      'lONWMMMWWNWWWMMMMM0,   .o0NMMMMMMMMMMMWNX0o.          'ldkXMMMMK,  .,lkKNWMMMMMMMMMWWMWNNWNOc.               
                .dNMMMMNd.  ,OWNx.     .:OKXXWMNOdlldOXMMMMWo   .co0MMMWKxollc:;'..          ,kNMMMMMMMMO. .dNWMMMMMMMMMMMNOddoc;,,,.                 
                lNMMMMNo.  .,kN0dll:.    c0XNMMK;    ;KMMMMNc     ;KMMMXl                  .cXMMMMMMMMMWo.'o0NWMMWWMMMMMMM0'                          
               ;KMMMWKl',lx0NWMMMXx:.   .dWMMMM0'  .c0WMMMNx.    .xMMMMWOodxxkOOdc.       'xNMMMMMMMMMMNc...,dxoccxNMMMMMNo                           
              ,0MMMWNOdONWMMMMMMWd.     .OMMMMWd..:OWMMMNk;      ;KMMMMMMMMMMMMWKl.      ,0WMMWOokNMMMWk.        .xNMMMMWO'                           
             .OMMMMNXXXWMMMMMMMMWd.     cNMMMMXlc0WMMMNk;.      .xWMMMMMMMWWN0o:.       ;0WMMWx..oNMMMWo.        cXMMMMMXc                            
             lNMMMMXdlkNXO0NMMMWK:     .kMMMMMWNWMMMXk;.        :XMMMMMMWKxo:.      .';oKMMMMWXO0NMMMMMNO;      .kWMMMWWx.                            
            .oWMMMWKo';lokXMMMWXl.     :NMMMMMMMMNOl'           oWMMMMKo;.      ...lOXWMMMMMMMMMMMMMMMMWk'      ,0MMMMW0;                             
             lXMMMWXd;lONMMMMMNx.     .kMMMMMMMMW0l'.          .kMMMMWl  .cdxkkkl..dNMMMMMMMWNNXNMMMMMXd;.      ,KMMMMWd.                             
             cXMMMMMNNWMMMMMMMXl      lNMMMMMMMMMMWN0d,.       ,KMMMWNxcxKWMMWXo.  .,xNMMWXOol:;xWMMMWd.        ;XMMMMX:                              
             ,0MMMMMMMMMWKXMMMK:     .dWMMMWK0KXNWWMMMNO;      ,0MMMMWWWMMMMNx,      cNMXx,.    ;XMMMNc         cNMMWXd.                              
              ,kNMMMMWKx;.cXMM0,      dWMMMK; ..,:oxxONWk.     .xWMMMMMMMXko;.       .kXl.      .dWMMX:         :NMMNO:                               
               .,cool;.   .oXWx.      oWMWWo         .;kO;      .:dOKXKkl'            .'.        ,KMMK,         ,0WN0k;                               
                            ,dd.      cNKo;.            .           ...                          .oNMk.         .oXO;.                                
                              .       .;'                                                         'O0,           'o;                                  
                                                                                                  .o;             .                                   
                                                                                                   ..                                                 

""")

def player_1_title():
    print("""                                                                                                                                                      
                                                                                                         
                                         ...                .''..              ..                                                                     
                                       ,kKx'              .oKXKOk;           .l0Ko.                                                                   
                   ..,:loodddl;.     .dXMK:             .,kWMMMMMXl.       .;kNMWXo,;looxkkdoc.      .,;:;:clollc,.                 ...co,            
              .,ldk0XWWMMMMMMMNO;  .:0WMWO:.         ..;OKOXMMMWWMk.      cOXMMMMMWNWMMMMMMMMWKl..;oOXWWMMMMMMMMMN0:.               ckOXO,            
            .cONMMWMMMMWWMMMMMMMNl.lNMMMWXl       .lONNNWW0ONMMMMMX:     :KMMMMWWWMMMMMWNXXXKkdddOWMMWMMMMMWMMMMMMMNc              :KMMM0,            
             'oKNNWMMKo;;:o0WMMMMOxXMMMMWx.      :0WMMMMMMW0KWMMMMMk. .:ONMMMMW00WMMMKl;'....   'xXNNWWWk:;;cdXMMMMWo             :XMMMM0,            
              .xWMMMMk.   .OWMMMMWWMMMMMO'     .oNMMMMMMMMMN0KWMMMMK; cXMMMMMM0xXMMMMO,.,;;;'.   ,KWMMMX:   .cXMMMMX;            :KMMMMWd.            
              ,KMMMMWd. .:OWMMMNKNMMMMMX:     .xWMMMMMMMMMMWOkNMMMMWkdXMMMMMM0o0MMMMMWXNWWWWNO;  oWMMMMK,  ,kNMMMW0:            '0MMMMWx.             
              ,KMMMMXc.c0WMMMWOcdNMMMMWd.    'OWMMMWOxKMMMMXc;KMMMMMWWMMMMMMKcoNMMMMMMMMMMWKx,  .OMMMMWx.;xNMMMWKl.             lNMMMMO.              
              lNMMMMXk0WMMMWKl.,0MMMMMO'    ,OWMMMMNxlOWMMMNkcdXMMMMMMMMMMX0c'OMMMMMMMMMNk;.    cNMMMMW00NMMMW0l.              .kMMMMX;               
             .xWMMMMMMMMMNkc.  lNMMMMX:.'cdkKWMMMMMMMMMMMMMMWk';ONWMMMMMMNl..:XMMMMMNKxc,.     .kMMMMMMMMMMNkc.                .OMMMWo                
             '0MMMMMMMN0o'    .kMMMMMk..kWMMMMMMMMMMMMMMMMMWXc  .xWMMMMMWd.  dWMMMMXc. .,;;cc' :XMMMMMMMMXd,                   .OMMM0,                
            .dWMMMMNkc'.      .kMMMMNl  :OXMMMWWNNKO0NMMMMNd'    cNMMMMWx.  .OMMMMMk''l0WWWXl.;0MMMMMMMMMN0xc'.                ;XMMWo                 
            '0MMMMWx.         .dNMMMWOoxO0XMMMXx:,'.'OMMMMK;     :XMMMWO'   .OMMMMMX0NMMMNk, .oNMMMMMMMMMMMMMNOl.              ,0MMNc                 
            .dWMMMNc           ;OWMMMMMMMMMMWO:.     lNMMMO.    .kWMMWO'    .dWMMMMMMMMW0c.   .xWMMWOccox0NWNWMWx.              lXM0,                 
             :XMMM0'          ,xXMMMMMMMXOdxd'       .kWMMx.    :NMMWO'      .dKNMMMWXk:.     .OMMMK;    .';;cOWX:              .dWK,                 
             ,KMNKo.        .oXMMMMMMNOc'             lWMWl     :O0NO'         .,:cc:.        .OMXKo.         .:l'               .dO:                 
             .lOc..         .lxOKNN0l,                ,KWK;     ..'l;                         .lk:..                               .'                 
               .               ..'..                   lO;                                                                                            
                                                       .:.                                                                                            
""")

def player_2_title():
    print("""                                                                                                                                                      
                                                                                          
                                                           .,'.                                                                                       
                                                        .cOKKOd:.       'd00x'                                             .                          
                       .,cooodkkxo:.    :dx:           .xWMMMMWNd.     cKMMMWOccodxxdl:'.    .':cccccccc;.             ..'lo. .'':c.                  
                   .,lkKNMMMMMMMMMWk' .cKMNk'       .;:d0NMMMMWWo     :XMMMMMWWMMMMMMMMNk:;okKNMMMMMMMMMWx.           .xKKXx..dKKXx.                  
                   'kNWWWMN0OOKNMMMWkcOWMMWk.     ;kXWMWX0KWMMMMk.  .oXMMMNKNMMMN0kddol:;:kWWWWWXOOOXWMMMWl          .kWMMWOlxNMMW0;                  
                    ,kWWMMk.  'OWMMMXXMMMM0,    .lXMMMMMMN00NMMMWo 'OWMMMXOOXMMMx.....    ;0WWMX:  .lXMMMX:         .kWMMMNO0WMMMWk.                  
                    '0MMMWd. 'xWMMWXNMMMMNc    .dWMMMMMMMMNO0MMMM0lkWMMMXx0WMMMMXO0KKKkc. cNMMM0, .lKMMMXo.         oNMMMWkxNMMMWx.                   
                    ,KMMMNc'oKWMMXddXMMMWx.   .dWMMWOONMMMKcdWMMMWWWMMMNodNMMMMMMMMMNKo' .kMMMWx,c0WMMNx,          '0MMMMOcOMMMM0'                    
                    cNMMMN0KWMMNk,.xMMMM0,  .'dNMMMW00WMMMNxlkWMMMMMMMWd;kMMMMMMMWXx;.   :XMMMWKKWMMNk,            cNMMMX::XMMMXc                     
                   .dWMMMMMMW0o'  ;KMMMNl.:k0XWMMMMMMMMMMMMX:.oXMMMMMWx.;XMMMMW0d:'.    .dWMMMMMMW0o'              oWMMWd.lWMMWx.                     
                   '0MMMMN0o;.    lWMMM0'.dNWMMMMWWNNWMMMW0l. .dWMMMWO. oWMMMM0, ,oxkx;.:XMMMMMMWKl.               lNMMK, oWMMX:                      
                   lWMMMK:.      .dWMMM0ccd0NMMNOdc;cKMMMK;   .xWMMM0, .xMMMMMKxkNMWKl.,0MMMMMMMMMWXk;.            ;XMMk. :NMMO.                      
                   lNMMMx.        ,kWMMWWMMMMMKl.   .dWMMO.   ,0MMM0;   oWMMMMMMMMNx'  '0MMMNxoxOXWWWNk.           'OWWo  .xWMk.                      
                   ;KMMNc        .lKWMMMMWKkdd,      ,0MMx.   :XMM0;    .d0XNWWNKd,    .OMMWx.   .;;cONd.           'kWo   .xWk.                      
                   .OW0d'       .dNWMMWXx:.           lWWo    ,d00:       ..';;,.      .kW0x,        .;,             'dl.   .oo.                      
                    'c.         .;coxxc.              ;KO'     .,:.                     ':.                            .      ..                      
                                                      .c;                                                                                             
                                                       ..                                                                                             
""")



########################################################################################################################
########################################################################################################################



def boot():
    # This emulates a boot screen on an Arcade Machine
    print("Insert Coin")
    input()
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)


def menu():
    # Displays options to user
    print("Please select from the following menu:\n"
          "1: FIGHT\n"
          "2: RULES\n"
          "9: Quit")
    print("Please enter your selection:")


def rules():
    #Displays rules of the game
    print("\nScript Fighter is a turn based fighting game.\n"
          "Think of it as a 4 option rock-paper-scissors.")
    input("↓")
    print("Each fighter has 100 health points, denoted as: ")
    print(_HEALTH100)
    input("↓")
    print("When you, or your opponent takes damage, health is taken away. \n"
          "In this example you eat a big High Attack (2) that does 30 damage: \n")
    print(_HEALTH70)
    input("↓")
    print("Your options are the same as your opponents, and they work as follows: \n"
          "1: High Block - This blocks High Attacks (punches), but is weak to Low Attacks (kicks)\n"
                          "2: High Attack (Punch) - This deals a whopping 30 damage, but will lose to Low Attacks (kicks) and nullified by High Block\n"
                          "3: Low Block - If this blocks a Low Attack (kick) it parries and deals 20 damage, although it is weak to High Attacks (punches)\n"
                          "4: Low Attack (Kick) - This deals 10 damage and evades High Attacks (punches), but is weak to Low Blocks\n"
                          "9: MAIN MENU - This brings you back to the Title Screen\n")
    input("↓")
    print("Now prepare for the next battle!")
    input("↓")


def selection_validation():
    #Checks for valid inputs by player
    while True:
        user_input = input()
        try:
            result = int(user_input)
            if result == 1 or result == 2 or result == 9:
                return result
            else:
                print("Invalid selection: ")
                print("Please choose an option from the menu above")
        except ValueError:
            print("Invalid selection: ")
            print("Please choose an option from the menu above")


def local_co_op(player1, player2):
    #Places the ASCII art fighters next to each other depending on what move is called
    #This was created with the help of AI, but the code is written by myself
    player1lines = player1.split('\n')
    player2lines = player2.split('\n')

    max_lines = max(len(player1lines), len(player2lines))

    for i in range(max_lines):
        if i < len(player1lines):
            line1 = player1lines[i]
        else:
            line1 = ''
        if i < len(player2lines):
            line2 = player2lines[i]
        else:
            line2 = ''
        print(line1 + line2)

def health_meter(health):
    #Calculates what health bar to display
        if health >= 100:
            return _HEALTH100
        elif health == 90:
            return _HEALTH90
        elif health == 80:
            return _HEALTH80
        elif health == 70:
            return _HEALTH70
        elif health == 60:
            return _HEALTH60
        elif health == 50:
            return _HEALTH50
        elif health == 40:
            return _HEALTH40
        elif health == 30:
            return _HEALTH30
        elif health == 20:
            return _HEALTH20
        elif health == 10:
            return _HEALTH10
        elif health <= 0:
            return _HEALTH0


def select_warning():
    #Warns the user of an invalid input
    print("Invalid selection: ")
    print("Please choose an option from the menu above. \n")


def player_action():
    #Displays player move options and returns valid inputs
    while True:
        try:
            move = int(input("------" + player1_name + "------\n"
                                  "1: High Block \n"
                                  "2: High Attack (Punch)\n"
                                  "3: Low Block \n"
                                  "4: Low Attack (Kick)\n"
                                  "9: MAIN MENU \n"))
            if move in [1, 2, 3, 4]:
                return move
            elif move == 9:
                main()
            else:
                select_warning()
        except ValueError:
            select_warning()

def player2():
    # Displays player move options and returns valid inputs
    while True:
        try:
            move = int(input("------" + player2_name + "------\n"
                             "1: High Block \n"
                             "2: High Attack (Punch)\n"
                             "3: Low Block \n"
                             "4: Low Attack (Kick)\n"
                             "9: MAIN MENU \n"))
            if move in [1, 2, 3, 4]:
                return move
            elif move == 9:
                main()
            else:
                select_warning()
        except ValueError:
            select_warning()

def kenneth():
    #determines and returns what the AI will do if Kenneth is chosen
    move = random.randint(1, 4)
    return move

def dean():
    #determines and returns what the AI will do if Dean is chosen
    #AI taught me what "random.choice" is. I was trying to use randint for my distribution. All code is written by myself
    dean_moves = [1, 1, 2, 2, 2, 2, 3, 3, 4]
    move = random.choice(dean_moves)
    return move

def talon():
    #determines and returns what the AI will do if Talon is chosen
    # AI taught me what "random.choice" is. I was trying to use randint for my distribution. All code is written by myself
    talon_moves = [1, 2, 2, 3, 3, 4, 4, 4, 4]
    move = random.choice(talon_moves)
    return move

def mode_select():
    #Allows the user to choose what mode they want to play
    while True:
        try:
            mode = int(input("SELECT MODE:\n"
                             "1: CPU VS\n"
                             "2: PLAYER VS PLAYER\n"
                             "9: MAIN MENU\n"))
            if mode in [1, 2, 9]:
                return mode
            else:
                select_warning()
        except ValueError:
            select_warning()

def choose_opponent():
    #Allows the user to choose what AI opponent to fight
    while True:
        try:
            opponent_choice = int(input("CHOOSE YOUR OPPONENT:\n"
                                 "1: KENNETH APPRENTICE - An all around fighter\n"
                                 "2: DEAN EARWICKER - A hard hitting boxer\n"
                                 "3: TALON - An evasive Taekwondo master\n"
                                 "9: MAIN MENU\n"))
            if opponent_choice in [1, 2, 3, 9]:
                return opponent_choice
            else:
                select_warning()
        except ValueError:
            select_warning()

def quit():
    #ends program and shows stats of player playtime
    print("Thanks for playing!")
    print("Credits: \n"
          "Lead Developer: Matthew Courchaine \n"
          "Art Director: Matthew Courchaine \n"
          "Player Feedback Manager: Matthew Courchaine \n"
          "Annoying Desk Companion: Dory the Cat")
    print(f"STATS: \nWINS: {str(wins)}  \nLOSSES: {str(losses)}  \nTIES: {str(ties)}")
    sys.exit()


win_streak = 0
wins = 0
losses = 0
ties = 0

def tie(X,Y):
    #determines if a tie has taken place
    if X <= 0 and Y <= 0:
        tie_screen()
        global ties
        ties = ties + 1
        win_streak = 0
        input("Insert Coin")
        main()



def play_game(X):
    #Operates the main gameplay

    if X == 1:
        #Player chose to fight
        mode = mode_select()
        if mode == 1:
            global wins
            global losses
            global ties
            opponent_decision = choose_opponent()
            if opponent_decision == 1:
                opponent = kenneth
            elif opponent_decision == 2:
                opponent = dean
            elif opponent_decision == 3:
                opponent = talon
            elif opponent_decision == 9:
                main()

        elif mode == 2:
            opponent = player2
            global player2_name
            player2_name = input("Enter Player 2 Fighter Name: ")

        elif mode == 9:
            main()

        local_co_op(_PLAYER1HB, _PLAYER2HB)
        player1_health = 100
        player2_health = 100

        global win_streak #global was the idea of chatgpt to help my win_streak tracking, although I wrote the code


        if win_streak >= 5:
            print("--------    A NEW CHALLENGER    --------")
            input("↓")
            print("'HAHAHA, " + player1_name + ". You have shown your self to be a fierce combatant'")
            input("↓")
            print("'BUT YOU ARE NOTHING COMPARED TO ME!!!'\n"
                  "KENNETH JOURNEYMAN")
            print("The opponents HP grew to " + str(_KENNETH_JOURNEYMAN_HP) + "!!!")
            input("↓")
            player2_health = _KENNETH_JOURNEYMAN_HP
            opponent = kenneth


        while True:
            if player1_health > 0 and player2_health > 0:
                try:
                    p1 = player_action()
                    p2 = opponent()

                    if p1 == 9:
                        main()

                    elif p1 == 1 and p2 == 1:
                        local_co_op(_PLAYER1HB, _PLAYER2HB)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))


                    elif p1 == 1 and p2 == 2:
                        local_co_op(_PLAYER1HB, _PLAYER2HA)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 1 and p2 == 3:
                        local_co_op(_PLAYER1HB, _PLAYER2LB)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))

                    elif p1 == 1 and p2 == 4:
                        player1_health = player1_health - _LOW_ATTACK
                        local_co_op(_PLAYER1HB, _PLAYER2LA)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 2 and p2 == 1:
                        local_co_op(_PLAYER1HA, _PLAYER2HB)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))

                    elif p1 == 2 and p2 == 2:
                        player1_health = player1_health - _HIGH_ATTACK
                        player2_health = player2_health - _HIGH_ATTACK
                        local_co_op(_PLAYER1HA, _PLAYER2HA)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 2 and p2 == 3:
                        player2_health = player2_health - _HIGH_ATTACK
                        local_co_op(_PLAYER1HA, _PLAYER2LB)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 2 and p2 == 4:
                        player1_health = player1_health - _LOW_ATTACK
                        local_co_op(_PLAYER1HA, _PLAYER2LA)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 3 and p2 == 1:
                        local_co_op(_PLAYER1LB, _PLAYER2HB)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))

                    elif p1 == 3 and p2 == 2:
                        player1_health = player1_health - _HIGH_ATTACK
                        local_co_op(_PLAYER1LB, _PLAYER2HA)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 3 and p2 == 3:
                        local_co_op(_PLAYER1LB, _PLAYER2LB)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 3 and p2 == 4:
                        player2_health = player2_health - _LOW_BLOCK
                        local_co_op(_PLAYER1LB, _PLAYER2LA)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 4 and p2 == 1:
                        player2_health = player2_health - _LOW_ATTACK
                        local_co_op(_PLAYER1LA, _PLAYER2HB)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 4 and p2 == 2:
                        player2_health = player2_health - _LOW_ATTACK
                        local_co_op(_PLAYER1LA, _PLAYER2HA)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 4 and p2 == 3:
                        player1_health = player1_health - _LOW_BLOCK
                        local_co_op(_PLAYER1LA, _PLAYER2LB)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                    elif p1 == 4 and p2 == 4:
                        player1_health = player1_health - _LOW_ATTACK
                        player2_health = player2_health - _LOW_ATTACK
                        local_co_op(_PLAYER1LA, _PLAYER2LA)
                        local_co_op(health_meter(player1_health), health_meter(player2_health))
                        tie(player1_health, player2_health)

                except ValueError:
                    select_warning()

            elif player1_health <100 and player1_health >= 20 and player2_health <= 0: # player 1 win default
                if mode ==1:
                    default_win_screen()
                    win_streak = win_streak + 1
                    wins = wins + 1
                    print("WINS STREAK: " + str(win_streak))
                elif mode == 2:
                    player_1_title()
                    default_win_screen()

                input("↓")
                main()


            elif player1_health <= 0 and player2_health >= 20 and player2_health < 100: # player 2 win default
                if mode == 1:
                    lose_screen()
                    win_streak = 0
                    losses = losses + 1
                    input("Insert Coin")
                elif mode == 2:
                    player_2_title()
                    default_win_screen()
                    input("↓")
                main()

            elif player1_health <= 0 and player2_health >= 100: #player 2 perfect KO
                if mode == 1:
                    perfect_screen()
                    lose_screen()
                    win_streak = 0
                    losses = losses + 1
                    input("Insert Coin")
                elif mode == 2:
                    player_2_title()
                    perfect_screen()
                    input("↓")
                main()

            elif player1_health >= 100 and player2_health <= 0: #player 1 perfect KO
                if mode == 1:
                    perfect_screen()
                    default_win_screen()
                    win_streak = win_streak + 1
                    wins = wins + 1
                    print("WINS STREAK: " + str(win_streak))
                elif mode == 2:
                    player_1_title()
                    perfect_screen()
                input("↓")
                main()

            elif player1_health < 100 and player1_health < 20 and player1_health > 0  and player2_health <= 0: #player 1 great
                if mode == 1:
                    great_screen()
                    default_win_screen()
                    win_streak = win_streak + 1
                    wins = wins + 1
                    print("WINS STREAK: " + str(win_streak))
                if mode == 2:
                    player_1_title()
                    great_screen()
                input("↓")
                main()

            elif player2_health < 100 and player2_health < 20 and player2_health > 0  and player1_health <= 0: #player 2 great
                if mode == 1:
                    lose_screen()
                    win_streak = 0
                    losses = losses + 1
                    print("WINS STREAK: " + str(win_streak))
                if mode == 2:
                    player_2_title()
                    great_screen()
                input("↓")
                main()

    elif X == 2:
        rules()
        main()

    elif X == 9:
        quit()


def main():

    title()
    menu()
    user_selection = selection_validation()
    play_game(user_selection)


boot()

player1_name = input("Enter Player 1 Fighter Name: ")

if __name__ == '__main__':
    main()

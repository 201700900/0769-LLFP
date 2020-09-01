import pandas as pd
import webbrowser
import json

def reportar():
    data=[]
    file = open("registro.json")
    array = json.loads(file.read())

    for nuevo in array:
        data.append(nuevo)

    df= pd.DataFrame(data=data)
    header="""<!DOCTYPE html>
                        <html>
                        <head>
                            <!-- Required meta tags -->
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <!-- Bootstrap CSS -->
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <title>REPORTE</title> 
                            <meta charset="utf-8"> 
                            <link href="https://fonts.googleapis.com/css?family=Poppins:400,700" rel="stylesheet">
                            <link rel="icon" type="image/png" href="icon.png" />
                            <style>
                                html, body{ height: 70%; } 
                                body{
                                    background-color: #DDECF4; 
                                    background-size: 100%; 
                                    font-family: 'Poppins'; 
                                    font-weight: 300; 
                                    height: 100%; 
                                    text-align: center; 
                                    color:#262B34;
                                }
                                .bold{
                                font-weight: 300;
                                }
                                #mi_tabla{
                                    margin: 150px
                                    overflow:auto;
                                    height:500px;
                                    width:auto; 
                                    padding:0px;
                                    }
                                    table  { border-collapse: collapse; width: 100%; }+
                                    thead { margin-top:-10px}
                                    .tableFixHead    { overflow-y: auto; height: 100px; }
                                    .tableFixHead th { position: sticky; top: 0; }
                                table{
                                    background-color: white;
                                    text-align:left;
                                    width: 100%
                                    border-collapse: collapse;    
                                }
                                th, td{
                                    padding: 20px;
                                }
                                thead{
                                    background-color: #246355;
                                    border-bottom: solid 5px #0F362D;
                                    color white;
                                }
                                tr:nth-child(even){
                                    background-color: #ddd;
                                }
                                tr:hover td{
                                    background-color: #369681;
                                    color: white;
                                }    
                            </style> 
                            </head> 
                            <body>
                                <div style="padding-top: 80px;">
                                    <div>
                                        <p style="font-size:2.4em; color: #1BBC9B;margin: 0px;" class="bold"> TAREA 4 </p>
                                        <h2 style="max-width: 600px; margin: 25px auto; font-size:3em;" class="bold"> REPORTE </h2>
                                    </div>    
                                </div>
                                <div class = "container" id="mi_tabla">"""
    tabla= df.to_html()
    footer="""</div>
                </body>
                </html> """
    html = header+tabla+footer
    f=open('reporte.html','wb')
    f.write(bytes(html, 'utf-8'))
    f.close()
    webbrowser.open_new_tab("reporte.html")
    
reportar()    
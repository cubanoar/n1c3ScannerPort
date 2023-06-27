# n1c3ScannerPort 

##Simple TCP Scanner Port

git clone https://github.com/cubanoar/n1c3ScannerPort.git

Ejemplos de uso:

            -Escaneo a los 51 puertos más usados:  
                        python port_scanner.py -t 127.0.0.1 -f

            -Especificar los puertos separados por (,) [80,8080]:  
                        python port_scanner.py -t 127.0.0.1 -p 21,23,443

            -Escanea un rango de puertos:  
                        python port_scanner.py -t 127.0.0.1 -ip 70 -ep 100
            
            -Escanea puertos por defecto [default 1-65536]:  
                        python port_scanner.py -t 127.0.0.1
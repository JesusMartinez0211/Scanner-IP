import nmap

scanner = nmap.PortScanner()

ip = input("Inserte una direccion IP")
print("La dirección IP que ingresaste fue:",ip)
scanner.scan(ip)

print(scanner.all_hosts())
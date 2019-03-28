sudo cp -a Enote /opt/
sudo chmod 7777 /opt/Enote
sudo cp enote /bin/

echo "Escoja su distribución"
echo " "
echo "1. Archlinux o derivadas"
echo "2. Debian o derivadas"
echo "3. Otra"
echo " "
read dist
case $dist in
    1)
        sudo pacman -S python-pip
        ;;
    2)
        sudo apt install python-pip
        ;;
    3)
        echo "Debe instalar manualmente pip de python, el paquete puede encontrarlo con el nombre: python-pip"
        ;;
    *)
        echo "Opción inválida"
        ;;
esac
    
echo "Enote ha sido instalado con éxito."

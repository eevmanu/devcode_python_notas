## Capítulo 10. Configuración de ambiente para desarrollo y editor de texto (ST3)

### Video 1

#### Ambiente de desarrollo en Linux

- Ambientes aislado
    - Necesidad de un paquete en diferentes versiones
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) y [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- Proceso de instalación
    - Verificar que **python** esta instalado, en su versión 3 de preferencia

            $ python3
            Python 3.X.X (default, XXX XX XXXX, XX:XX:XX)
            [GCC 4.X.X] on linux
            Type "help", "copyright", "credits" or "license" for more information.
            >>>

    - Verificar que **pip3** (gestor de paquetes Python 3) esta instalado

            $ pip3
            Usage:
            pip3 <command> [options]
            ...

    - Si no esta instalado, instalarlo

            $ (sudo) apt-get install python-pip3

    - Actualizar paquetes claves

            $ (sudo) pip3 install -U pip setuptools wheel

    - Instalar virtualenv

            $ (sudo) pip3 install -U virtualenv

    - Instalar virtualenvwrapper

            $ (sudo) pip3 install -U virtualenvwrapper

    - Modificar el archivo de configuración del terminal (~/.bashrc en Ubuntu y LinuxMint)

            export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
            export WORKON_HOME=$HOME/Envs
            mkdir -p $WORKON_HOME
            source /usr/local/bin/virtualenvwrapper.sh

    - [Opcional] Activar la definición del **locale** a utilizar (en caso surja este [error](http://stackoverflow.com/a/36394262/3889948))

            export LC_ALL=C


#### Editor de texto - Sublime text 3

- Descargar e instalar [Sublime Text 3](https://www.sublimetext.com/3)
- Instalar **PackageControl** (gestor de paquetes en ST3), instrucciones [aquí](https://packagecontrol.io/installation#st3)
- Instalar los siguientes paquetes (recomendación personal)
    - Anaconda
    - BracketHighlighter
    - SideBarEnhancements
    - TrailingSpaces
    - Git
    - WakaTime

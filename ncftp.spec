Summary:     Browser program for the File Transfer Protocol
Summary(de): ftp-Client mit einer attraktiven Bedineroberfläche
Summary(fr): Client ftp avec une interface agréable.
Summary(pl): Zaawansowany klient FTP
Summary(tr): Güzel arayüzlü bir ftp istemcisi
Name:        ncftp
Version:     2.4.3
Release:     5
Copyright:   GPL
Group:       Applications/Networking
Group(pl):   Aplikacje/Sieæ
Source0:     ftp://ftp.ncftp.com/pub/ncftp/%{name}-%{version}.tar.gz
Source1:     ncftp.wmconfig
BuildRoot:   /tmp/%{name}-%{version}-%{release}-root

%description
Ncftp is a ftp client with many advantageous over the standard one. It
includes command line editing, command histories, support for recurisive
gets, automatic logins, and much more.

%description -l de
Ncftp ist ein ftp-Client mit vielen Verbesserungen. Er enthält Funktionen wie
Befehlszeilenbearbeitung, Befehlsgeschichte, Unterstützung für rekursive
Ladevorgänge, automatische Logins, usw.

%description -l fr
Ncftp est un client ftp possédant de nombreux avantages sur le client
standard. Il inclue une edition de la ligne de commande, un historique
des commandes, un support pour des téléchargements récursifs, des logins
automatiques, et plus encore.

%description -l pl
NcFTP jest zaawansowanym klientem ftp. Pozwala na edytowanie lini komend,
zapamiêtuje komendy, potrafi pobieraæ ca³e katalogi wraz z podkatalogami z
serwerów ftp, automatycznie logowaæ siê itp. 

%description -l tr
Ncftp, standart ftp istemcisine oranla pek çok avantajý olan bir yazýlýmdýr.
Komut tarihçesi, rekürsif dosya aktarýmý, kendiliðinden sisteme giriþ gibi
yetenekleri vardýr.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/{bin,man/man1}}

install -s ncftp $RPM_BUILD_ROOT/usr/bin 
install ncftp.1 $RPM_BUILD_ROOT/usr/man/man1 

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/ncftp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/wmconfig/ncftp
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Fri Sep 04 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.4.3-1]
- added pl translation.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- compiled for Manhattan

* Fri Mar 20 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.4.3 for security reasons

* Wed Nov 05 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the spec file

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- updated to ncftp 2.4.2

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Donnie Barnes <djb@redhat.com>
- Rebuild as Sun version didn't work.

Summary:	Browser program for the File Transfer Protocol
Summary(de):	NcFTP - ein Textmodus FTP-Client
Summary(es):	Cliente ftp con una interface agradable
Summary(pl):	Zaawansowany klient FTP
Summary(pt_BR):	Cliente ftp com uma interface agradável
Name:		ncftp
Version:	3.1.7
Release:	3
Epoch:		2
License:	The Clarified Artistic License
Group:		Applications/Networking
Source0:	ftp://ftp.ncftp.com/ncftp/%{name}-%{version}-src.tar.bz2
# Source0-md5:	2a310a3c9ca126e6b409d0d1d1ccda75
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	ncftpbookmarks.1
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shared.patch
# based on:	ftp://ftp.kame.net/pub/kame/misc/%{name}-315-v6-20030207.diff.gz
Patch2:		ftp://ftp.kame.net/pub/kame/misc/ncftp-317-v6-20040108b.diff.gz
Patch3:		%{name}-sa_len.patch
Patch4:		%{name}-ac25x.patch
Patch5:		%{name}-libdir.patch
URL:		http://www.ncftp.com/
BuildRequires:	autoconf >= 2.53
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NcFTP is a ftp client with many advantages over the standard one. It
includes command line editing, command histories, support for
recursive gets, automatic logins, background downloading and much
more. This version supports IPv6, too.

%description -l es
ncftp es un cliente ftp con varias ventajas sobre el padrón. Incluye
edición por línea de comando, histórico de comandos, logins
automáticos, y mucho más.

%description -l pl
NcFTP jest zaawansowanym klientem ftp. Pozwala na edytowanie linii
komend, zapamiêtuje komendy, potrafi pobieraæ ca³e katalogi wraz z
podkatalogami z serwerów ftp, automatycznie logowaæ siê itp. Ta wersja
dodatkowo wspiera IPv6.

%description -l pt_BR
ncftp é um cliente ftp com várias vantagens sobre o padrão. Ele inclui
edição por linha de comando, histórico de comandos, logins
automáticos, e muito mais.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5

%build
ln -sf autoconf/aclocal.m4 .
%{__autoconf}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--enable-ncurses \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_pixmapsdir},%{_mandir},%{_desktopdir}}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%{__make} -C libncftp soinstall \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt README.v6 doc/{CHAN*,FIRE*,LICENSE,READLINE,what*}.txt
%{_desktopdir}/ncftp.desktop
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%{_mandir}/man1/*
%{_pixmapsdir}/ncftp.png

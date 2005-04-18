Summary:	Browser program for the File Transfer Protocol
Summary(de):	NcFTP - ein Textmodus FTP-Client
Summary(es):	Cliente FTP con una interface agradable
Summary(pl):	Zaawansowany klient FTP
Summary(pt_BR):	Cliente FTP com uma interface agradável
Name:		ncftp
Version:	3.1.9
Release:	1
Epoch:		2
License:	The Clarified Artistic License
Group:		Applications/Networking
Source0:	ftp://ftp.ncftp.com/ncftp/%{name}-%{version}-src.tar.bz2
# Source0-md5:	66cf8dacec848eb11a70632fe9f21807
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	ncftpbookmarks.1
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shared.patch
Patch2:		ftp://ftp.kame.net/pub/kame/misc/ncftp-3181-v6-20040826.diff.gz
Patch3:		%{name}-ac25x.patch
Patch4:		%{name}-libdir.patch
URL:		http://www.ncftp.com/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NcFTP is a FTP client with many advantages over the standard one. It
includes command line editing, command histories, support for
recursive gets, automatic logins, background downloading and much
more. This version supports IPv6, too.

%description -l es
ncftp es un cliente FTP con varias ventajas sobre el padrón. Incluye
edición por línea de comando, histórico de comandos, logins
automáticos, y mucho más.

%description -l pl
NcFTP jest zaawansowanym klientem FTP. Pozwala na edytowanie linii
komend, zapamiêtuje komendy, potrafi pobieraæ ca³e katalogi wraz z
podkatalogami z serwerów FTP, automatycznie logowaæ siê itp. Ta wersja
dodatkowo wspiera IPv6.

%description -l pt_BR
ncftp é um cliente FTP com várias vantagens sobre o padrão. Ele inclui
edição por linha de comando, histórico de comandos, logins
automáticos, e muito mais.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4

%build
ln -sf autoconf/aclocal.m4 .
%{__autoconf}
CFLAGS="-I/usr/include/ncurses -Dss_family=__ss_family -Dss_len=__ss_len %{rpmcflags}"
CPPFLAGS="-I/usr/include/ncurses -Dss_family=__ss_family -Dss_len=__ss_len %{rpmcflags}"
%configure \
	--enable-ncurses \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_pixmapsdir},%{_mandir},%{_applnkdir}/Network/FTP}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%{__make} -C libncftp DESTDIR=$RPM_BUILD_ROOT soinstall

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/FTP
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt README.v6 doc/{CHAN*,FIRE*,LICENSE,READLINE,what*}.txt
%{_applnkdir}/Network/FTP/ncftp.desktop
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%{_mandir}/man1/*
%{_pixmapsdir}/ncftp.png

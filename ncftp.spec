# NOTE: update kame patch to use val_getaddrinfo() when/if enabling DNSSEC verification
Summary:	Browser program for the File Transfer Protocol
Summary(de.UTF-8):	NcFTP - ein Textmodus FTP-Client
Summary(es.UTF-8):	Cliente FTP con una interface agradable
Summary(pl.UTF-8):	Zaawansowany klient FTP
Summary(pt_BR.UTF-8):	Cliente FTP com uma interface agradável
Name:		ncftp
Version:	3.2.5
Release:	2
Epoch:		2
License:	The Clarified Artistic License
Group:		Applications/Networking
Source0:	ftp://ftp.ncftp.com/ncftp/%{name}-%{version}-src.tar.bz2
# Source0-md5:	b05c7a6d5269c04891f02f43d4312b30
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	ncftpbookmarks.1
# not updated yet, replaced by patch4
#Source4:	ftp://ftp.kame.net/pub/kame/misc/ncftp-323-v6-20091109.diff.gz
## Source4-md5:	9120dcbb0fceacb5174d01024b0ba5a5
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-ac25x.patch
Patch3:		%{name}-home_etc.patch
Patch4:		%{name}-kame-v6.patch
Patch5:		%{name}-ac.patch
URL:		http://www.ncftp.com/
BuildRequires:	autoconf >= 2.53
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libncftp.so.*

%description
NcFTP is a FTP client with many advantages over the standard one. It
includes command line editing, command histories, support for
recursive gets, automatic logins, background downloading and much
more. This version supports IPv6, too.

%description -l es.UTF-8
ncftp es un cliente FTP con varias ventajas sobre el padrón. Incluye
edición por línea de comando, histórico de comandos, logins
automáticos, y mucho más.

%description -l pl.UTF-8
NcFTP jest zaawansowanym klientem FTP. Pozwala na edycję linii poleceń,
zapamiętuje polecenia, potrafi pobierać całe katalogi wraz z
podkatalogami z serwerów FTP, automatycznie logować się itp. Ta wersja
dodatkowo wspiera IPv6.

%description -l pt_BR.UTF-8
ncftp é um cliente FTP com várias vantagens sobre o padrão. Ele inclui
edição por linha de comando, histórico de comandos, logins
automáticos, e muito mais.

%prep
%setup -q
#gunzip -c %{SOURCE4} | patch -p1
%patch4 -p1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1

%build
%{__autoconf} -I autoconf_local
%{__autoheader} -I autoconf_local
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_pixmapsdir},%{_mandir},%{_desktopdir},/var/spool/%{name}}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%{__make} -C libncftp soinstall \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1

# devel not used by anything
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libncftp.so
%{__rm} $RPM_BUILD_ROOT%{_includedir}/ncftp*.h

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt README.v6 doc/{CHANGELOG,FIREWALLS_AND_PROXIES,LICENSE,READLINE,what_*}.txt
%attr(755,root,root) %{_bindir}/ncftp*
%attr(755,root,root) %{_libdir}/libncftp.so.*
%dir /var/spool/%{name}
%{_mandir}/man1/ncftp*.1*
%{_desktopdir}/ncftp.desktop
%{_pixmapsdir}/ncftp.png

Summary:	Browser program for the File Transfer Protocol
Summary(pl):	Zaawansowany klient FTP
Name:		ncftp
Version:	3.0beta21
Release:	2
Copyright:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ncftp.com/ncftp/3.0BETA/%{name}-%{version}-src.tar.gz
Source1:	ncftp.desktop
Patch0:		ncftp-noroot.patch
Patch1:		ncftp-DESTDIR.patch
Patch2:		ftp://ftp.kame.net/pub/kame/misc/ncftp-30b19-19990719.diff.gz
Patch3:		ncftp-pld.patch
Patch4:		ncftp-shared.patch
URL:		http://www.ncftp.com/
BuildRequires:	readline-devel >= 4.1
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	/tmp/%{name}-%{version}-root

%description
NcFTP is a ftp client with many advantages over the standard one. It
includes command line editing, command histories, support for recursive
gets, automatic logins, background downloading and much more. This
version support IPv6, too.

%description -l pl
NcFTP jest zaawansowanym klientem ftp. Pozwala na edytowanie lini komend,
zapami�tuje komendy, potrafi pobiera� ca�e katalogi wraz z podkatalogami z
serwer�w ftp, automatycznie logowa� si� itp. Ta wersja dodatkowo wspiera IPv6.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

%build
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-ipv6

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir},/usr/X11R6/share/applnk/Networking}

make DESTDIR=$RPM_BUILD_ROOT install
make -C libncftp DESTDIR=$RPM_BUILD_ROOT soinstall

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Networking

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/* \
	BETA-README WHATSNEW-3.0

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BETA-README.gz WHATSNEW-3.0.gz
/usr/X11R6/share/applnk/Networking/ncftp.desktop
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%{_mandir}/man1/*

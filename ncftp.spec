Summary:	Browser program for the File Transfer Protocol
Summary(pl):	Zaawansowany klient FTP
Name:		ncftp
Version:	3.0.1
Release:	1
Copyright:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ncftp.com/ncftp/%{name}-%{version}-src.tar.gz
Source1:	ncftp.desktop
Patch0:		ncftp-DESTDIR.patch
Patch1:		ncftp-shared.patch
Patch2:		ncftp-301-v6-20000407.diff.gz
URL:		http://www.ncftp.com/
BuildRequires:	readline-devel >= 4.1
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch2 -p1

%build
cp autoconf/aclocal.m4 .
autoconf
CPPFLAGS="-I/usr/include/ncurses"
LDFLAGS="-s"
export CPPFLAGS LDFLAGS
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

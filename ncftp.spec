Summary:	Browser program for the File Transfer Protocol
Summary(pl):	Zaawansowany klient FTP
Name:		ncftp
Version:	3.0.3
Release:	1
Epoch:		2
License:	The Clarified Artistic License
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ncftp.com/ncftp/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-302-v6-20001225.diff.gz
Patch3:		%{name}-sa_len.patch
URL:		http://www.ncftp.com/
BuildRequires:	readline-devel >= 4.1
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NcFTP is a ftp client with many advantages over the standard one. It
includes command line editing, command histories, support for
recursive gets, automatic logins, background downloading and much
more. This version supports IPv6, too.

%description -l pl
NcFTP jest zaawansowanym klientem ftp. Pozwala na edytowanie linii
komend, zapami�tuje komendy, potrafi pobiera� ca�e katalogi wraz z
podkatalogami z serwer�w ftp, automatycznie logowa� si� itp. Ta wersja
dodatkowo wspiera IPv6.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f autoconf/aclocal.m4 .
autoconf
CFLAGS="-I%{_includedir}/ncurses -Dss_family=__ss_family -Dss_len=__ss_len %{rpmcflags}"
CPPFLAGS="-I%{_includedir}/ncurses -Dss_family=__ss_family -Dss_len=__ss_len %{rpmcflags}"
export CPPFLAGS
%configure \
	--enable-ncurses \
#	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir},%{_applnkdir}/Network/FTP}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%{__make} -C libncftp DESTDIR=$RPM_BUILD_ROOT soinstall

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/FTP

gzip -9nf WHATSNEW-3.0 FIREWALL-PROXY-README CHANGELOG LICENSE.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_applnkdir}/Network/FTP/ncftp.desktop
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%{_mandir}/man1/*

Summary:	Browser program for the File Transfer Protocol
Summary(pl):	Zaawansowany klient FTP
Name:		ncftp
Version:	3.0beta19
Release:	1
Copyright:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieæ
Source:		ftp://ftp.ncftp.com/ncftp/3.0BETA/%{name}-%{version}-src.tar.gz
URL:		http://www.ncftp.com
Patch0:		ncftp-noroot.patch
Patch1:		ncftp-DESTDIR.patch
BuildPrereq:	readline-devel
BuildPrereq:	ncurses-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
NcFTP is a ftp client with many advantages over the standard one. It
includes command line editing, command histories, support for recursive
gets, automatic logins, background downloading and much more.

%description -l pl
NcFTP jest zaawansowanym klientem ftp. Pozwala na edytowanie lini komend,
zapamiêtuje komendy, potrafi pobieraæ ca³e katalogi wraz z podkatalogami z
serwerów ftp, automatycznie logowaæ siê itp. 

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
LDFLAGS="-s"; export LDFLAGS
%configure 

make -C libncftp shared
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}}

make DESTDIR=$RPM_BUILD_ROOT install
make -C libncftp DESTDIR=$RPM_BUILD_ROOT soinstall

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/* \
	BETA-README WHATSNEW-3.0

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BETA-README.gz WHATSNEW-3.0.gz

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%{_mandir}/man1/*

%changelog
* Thu Jun 24 1999 Michal Margula <alchemyx@pld.org.pl>
  [3.0beta19-1]
- upgraded to beta19
- spec corrected for FHS 2.0
- added BuildPrereq

* Fri Apr 23 1999 Maciej Le¶niewski <nimir@kis.p.lodz.pl>
  [3.0beta18-2]
- Gzipped docs
- Removed man group from man pages

* Wed Feb 24 1999 Maciej Le¶niewski <nimir@kis.p.lodz.pl>
  [3.0beta18-1]
- new version,
- updated noroot-patch,
- removed strip in %install macro - not needed.

* Mon Jan 04 1999 PLD-team <pld-list@mailbox.tuniv.szczecin.pl>
  [3.0beta16-2d]
- build for Linux PLD.

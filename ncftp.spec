Summary:	Browser program for the File Transfer Protocol
Summary(pl):	Zaawansowany klient FTP
Name:		ncftp
Version:	3.0beta18
Release:	2
Source:		ftp://ftp.ncftp.com/ncftp/3.0BETA/%{name}-%{version}-src.tar.gz
Patch:		%{name}-noroot.patch
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieæ
Copyright:	GPL
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
%setup -q
%patch -p1

%build
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
    ./configure \
	--prefix=/usr

make -C libncftp CFLAGS="$RPM_OPT_FLAGS" shared
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib
make prefix=$RPM_BUILD_ROOT/usr install
make -C libncftp SOLIBDIR=$RPM_BUILD_ROOT/usr/lib soinstall

gzip -9fn $RPM_BUILD_ROOT/usr/man/man1/* BETA-README WHATSNEW-3.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BETA-README.gz WHATSNEW-3.0.gz

%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/*.so*
/usr/man/man1/*

%changelog
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
- build for Linux PLD,
- major changes.

* Thu Dec 03 1998 Arne Coucheron <arneco@online.no>
  [3.0beta16-1]

* Fri Nov 06 1998 Arne Coucheron <arneco@online.no>
  [3.0beta15-1]

* Thu Jun 25 1998 Arne Coucheron <arneco@online.no>
  [3.0beta14-1]

* Tue Jun 23 1998 Arne Coucheron <arneco@online.no>
  [3.0beta13-1]
- small changes to the spec file

* Sun Jun 07 1998 Arne Coucheron <arneco@online.no>
  [3.0beta12-1]
- added -q parameter to %setup
- using %defattr macro in filelist
- using %%{name} and %%{version} macros

* Tue May 12 1998 Arne Coucheron <arneco@online.no>
  [3.0beta11-1]

* Mon May 04 1998 Arne Coucheron <arneco@online.no>
  [3.0beta10-1]

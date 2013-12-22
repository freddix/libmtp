Summary:	Implementation of Microsoft's Media Transfer Protocol (MTP)
Name:		libmtp
Version:	1.1.6
Release:	4
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libmtp/%{name}-%{version}.tar.gz
# Source0-md5:	87835626dbcf39e62bfcdd4ae6da2063
URL:		http://libmtp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusbx-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmtp is an implementation of Microsoft's Media Transfer Protocol
(MTP) in the form of a library suitable primarily for POSIX compliant
operating systems.

%package devel
Summary:	Header files for mtp library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for mtp library.

%package examples
Summary:	Examples based on mtp library
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description examples
Examples based on mtp library.

%package udev
Summary:	UDev rules and mtp-probe utility
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	udev
Obsoletes:	libmtp-progs

%description udev
UDev MTP rules and mtp-probe utility.

%prep
%setup -q

%{__sed} -i "s|AM_CONFIG_HEADER|AC_CONFIG_HEADERS|" configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-static		\
	--with-udev=/usr/lib/udev	\
	--with-udev-group=audio		\
	--with-udev-mode=0660
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -i '1,3d' $RPM_BUILD_ROOT%{_prefix}/lib/udev/rules.d/69-libmtp.rules

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %ghost %{_libdir}/libmtp.so.?
%attr(755,root,root) %{_libdir}/libmtp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmtp.so
%{_libdir}/libmtp.la
%{_includedir}/libmtp.h
%{_pkgconfigdir}/libmtp.pc

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mtp-albumart
%attr(755,root,root) %{_bindir}/mtp-albums
%attr(755,root,root) %{_bindir}/mtp-connect
%attr(755,root,root) %{_bindir}/mtp-delfile
%attr(755,root,root) %{_bindir}/mtp-detect
%attr(755,root,root) %{_bindir}/mtp-emptyfolders
%attr(755,root,root) %{_bindir}/mtp-files
%attr(755,root,root) %{_bindir}/mtp-filetree
%attr(755,root,root) %{_bindir}/mtp-folders
%attr(755,root,root) %{_bindir}/mtp-format
%attr(755,root,root) %{_bindir}/mtp-getfile
%attr(755,root,root) %{_bindir}/mtp-getplaylist
%attr(755,root,root) %{_bindir}/mtp-hotplug
%attr(755,root,root) %{_bindir}/mtp-newfolder
%attr(755,root,root) %{_bindir}/mtp-newplaylist
%attr(755,root,root) %{_bindir}/mtp-playlists
%attr(755,root,root) %{_bindir}/mtp-reset
%attr(755,root,root) %{_bindir}/mtp-sendfile
%attr(755,root,root) %{_bindir}/mtp-sendtr
%attr(755,root,root) %{_bindir}/mtp-thumb
%attr(755,root,root) %{_bindir}/mtp-tracks
%attr(755,root,root) %{_bindir}/mtp-trexist

%files udev
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/lib/udev/mtp-probe
%{_prefix}/lib/udev/rules.d/69-libmtp.rules


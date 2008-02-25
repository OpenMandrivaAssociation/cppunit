%define major 1
%define api 1.12
%define libname %mklibname cppunit %{api}_%{major}
%define develname %mklibname cppunit -d
%define testrunnermajor 1
%define testrunnerlibname %mklibname qttestrunner %testrunnermajor

Summary:	C++ Port of JUnit Testing Framework
Name:		cppunit
Version:	1.12.1
Release:	%mkrel 1
License:	LGPL
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.gz
Patch:		cppunit-1.11.4-missing-include.patch.bz2
URL:		http://cppunit.sourceforge.net/
BuildRequires:	qt3-devel
BuildRequires:	doxygen
BuildRequires:	automake1.7
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
CppUnit is the C++ port of the famous JUnit framework for unit
testing. Test output is in XML for automatic testing and GUI
based for supervised tests.

%package -n	%{libname}
Summary:	C++ Port of JUnit Testing Framework
Group:          System/Libraries

%description -n	%{libname}
CppUnit is the C++ port of the famous JUnit framework for unit
testing. Test output is in XML for automatic testing and GUI
based for supervised tests.

%package -n %testrunnerlibname
Summary:	QT Testrunner for %name
Group:		System/Libraries

%description -n %testrunnerlibname
CppUnit is the C++ port of the famous JUnit framework for unit
testing. Test output is in XML for automatic testing and GUI
based for supervised tests.


%package -n	%{develname}
Summary:	Development files for %{libname}
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	cppunit-devel = %{version}-%{release}
Provides:	libcppunit-devel = %{version}-%{release}
Provides:	libcppunit%{api}-devel = %{version}-%{release}
Obsoletes:	%{mklibname cppunit 1.12_0 -d}

%description -n	%{develname}
CppUnit is the C++ port of the famous JUnit framework for unit
testing. Test output is in XML for automatic testing and GUI
based for supervised tests.

%prep

%setup -q
%patch -p1

%build
%configure2_5x \
    --enable-doxygen 

%make
cd src/qttestrunner
qmake
make QTDIR=%_prefix/lib/qt3
%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall
cp -d lib/* %buildroot%_libdir

# clean up
rm -rf %{buildroot}%{_datadir}/cppunit
%if %mdkversion >= 1020
%multiarch_binaries %buildroot%_bindir/cppunit-config
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post -n %{testrunnerlibname} -p /sbin/ldconfig
%postun -n %{testrunnerlibname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS ChangeLog
%attr(755,root,root) %{_libdir}/libcppunit-%{api}.so.%{major}*

#%files -n %testrunnerlibname
#%defattr(-,root,root)
#%{_libdir}/libqttestrunner.so.%{testrunnermajor}*

%files -n %{develname}
%defattr(644,root,root,755)
%doc %_datadir/doc/cppunit
%attr(755,root,root) %{_bindir}/cppunit-config
%if %mdkversion >= 1020
%attr(755,root,root) %{multiarch_bindir}/cppunit-config
%endif
%attr(755,root,root) %{_bindir}/DllPlugInTester
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/cppunit
%{_datadir}/aclocal/cppunit.m4
%{_mandir}/man1/*
%_libdir/pkgconfig/cppunit.pc

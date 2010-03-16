%define major 1
%define api 1.12
%define libname %mklibname cppunit %{api}_%{major}
%define develname %mklibname cppunit -d
%define testrunnermajor 1
%define testrunnerlibname %mklibname qttestrunner %testrunnermajor

Summary:	C++ port of JUnit Testing Framework
Name:		cppunit
Version:	1.12.1
Release:	%mkrel 7
License:	LGPLv2+
Group:		System/Libraries
URL:		http://cppunit.sourceforge.net/
Source0:	http://downloads.sourceforge.net/cppunit/%{name}-%{version}.tar.bz2
Patch:		cppunit-1.11.4-missing-include.patch
Patch1:     cppunit-1.12.1-qt3-gcc43.patch
BuildRequires:	qt3-devel
BuildRequires:	doxygen
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CppUnit is the C++ port of the famous JUnit framework for unit
testing. Test output is in XML for automatic testing and GUI
based for supervised tests.

%package -n %{libname}
Summary:	C++ port of JUnit Testing Framework
Group:		System/Libraries

%description -n	%{libname}
CppUnit is the C++ port of the famous JUnit framework for unit
testing. Test output is in XML for automatic testing and GUI
based for supervised tests.

%package -n %{testrunnerlibname}
Summary:	QT Testrunner for %{name}
Group:		System/Libraries

%description -n %{testrunnerlibname}
CppUnit is the C++ port of the famous JUnit framework for unit
testing. Test output is in XML for automatic testing and GUI
based for supervised tests.


%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{name}%{api}-devel = %{version}-%{release}
Obsoletes:	%{mklibname cppunit 1.12_0 -d}

%description -n %{develname}
CppUnit is the C++ port of the famous JUnit framework for unit
testing. Test output is in XML for automatic testing and GUI
based for supervised tests.

%prep

%setup -q
%patch -p1
%patch1 -p1 -b .qt3

%build
%configure2_5x \
    --enable-doxygen 

# <oden> somehow LIBADD_DL is ignored, is that an intentional change?
perl -pi -e "s|^LIBS =.*|LIBS = -lm -ldl|g" src/cppunit/Makefile

%make

pushd src/qttestrunner
export QTDIR=%{qt3dir}
    %{qt3dir}/bin/qmake
    %make
popd

%install
rm -rf %{buildroot}

%makeinstall_std

cp -d lib/* %{buildroot}%{_libdir}

#(tpg) do not duplicate docs
rm -rf  %{buildroot}%{_datadir}/doc/cppunit

# clean up
rm -rf %{buildroot}%{_datadir}/cppunit
%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/cppunit-config
%endif

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{testrunnerlibname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{testrunnerlibname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libcppunit-%{api}.so.%{major}*

#%files -n %testrunnerlibname
#%defattr(-,root,root)
#%{_libdir}/libqttestrunner.so.%{testrunnermajor}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS ChangeLog
%{_bindir}/cppunit-config
%if %mdkversion >= 1020
%{multiarch_bindir}/cppunit-config
%endif
%{_bindir}/DllPlugInTester
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/cppunit
%{_datadir}/aclocal/cppunit.m4
%{_mandir}/man1/*
%{_libdir}/pkgconfig/cppunit.pc

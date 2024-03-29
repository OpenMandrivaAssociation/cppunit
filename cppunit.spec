%define major 1
%define api 1.15
%define libname %mklibname cppunit %{api}_%{major}
%define develname %mklibname cppunit -d

Summary:	C++ port of JUnit Testing Framework
Name:		cppunit
Version:	1.15.1
Release:	2
License:	LGPLv2+
Group:		System/Libraries
URL:		https://freedesktop.org/wiki/Software/cppunit/
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.gz
Patch0:		cppunit-1.11.4-missing-include.patch

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
%autopatch -p1

%build
%configure \
    --enable-shared \
    --disable-static \
    --disable-doxygen \
    --disable-dot \
    --disable-html-docs \
    --disable-latex-docs

# <oden> somehow LIBADD_DL is ignored, is that an intentional change?
perl -pi -e "s|^LIBS =.*|LIBS = -lm -ldl|g" src/cppunit/Makefile

%make_build

%install

%make_install

#(tpg) do not duplicate docs
rm -rf  %{buildroot}%{_datadir}/doc/cppunit

# clean up
rm -rf %{buildroot}%{_datadir}/cppunit
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_libdir}/libcppunit-%{api}.so.%{major}*

%files -n %{develname}
%doc AUTHORS NEWS README THANKS ChangeLog
%{_bindir}/DllPlugInTester
%{_libdir}/*.so
%{_includedir}/cppunit
%{_libdir}/pkgconfig/cppunit.pc

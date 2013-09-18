%define api	1.13
%define major	0
%define libname	%mklibname cppunit %{api} %{major}
%define devname	%mklibname cppunit -d

Summary:	C++ port of JUnit Testing Framework
Name:		cppunit
Version:	1.13.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.freedesktop.org/wiki/Software/cppunit/
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.gz
Patch0:		cppunit-1.11.4-missing-include.patch
Patch1:		cppunit-1.12.1-no_lib_in_cppunit-config.diff

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

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
CppUnit is the C++ port of the famous JUnit framework for unit
testing. Test output is in XML for automatic testing and GUI
based for supervised tests.

%prep

%setup -q
%apply_patches

%build
%configure2_5x \
	--enable-shared \
	--disable-static \
	--disable-doxygen \
	--disable-dot \
	--disable-html-docs \
	--disable-latex-docs

# <oden> somehow LIBADD_DL is ignored, is that an intentional change?
sed -i -e "s|^LIBS =.*|LIBS = -lm -ldl|g" src/cppunit/Makefile

%make

%install
%makeinstall_std

#(tpg) do not duplicate docs
rm -rf  %{buildroot}%{_datadir}/doc/cppunit

# clean up
rm -rf %{buildroot}%{_datadir}/cppunit
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_libdir}/libcppunit-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README THANKS ChangeLog
%{_bindir}/cppunit-config
%{_bindir}/DllPlugInTester
%{_libdir}/*.so
%{_includedir}/cppunit
%{_datadir}/aclocal/cppunit.m4
%{_mandir}/man1/*
%{_libdir}/pkgconfig/cppunit.pc


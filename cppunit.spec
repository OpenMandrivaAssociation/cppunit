%define major 1
%define api 1.12
%define libname %mklibname cppunit %{api}_%{major}
%define develname %mklibname cppunit -d
%define testrunnermajor 1
%define testrunnerlibname %mklibname qttestrunner %testrunnermajor

Summary:	C++ port of JUnit Testing Framework
Name:		cppunit
Version:	1.12.1
Release:	11
License:	LGPLv2+
Group:		System/Libraries
URL:		http://cppunit.sourceforge.net/
Source0:	http://downloads.sourceforge.net/cppunit/%{name}-%{version}.tar.bz2
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
%patch0 -p1
%patch1 -p0

%build
%configure2_5x \
    --enable-shared \
    --disable-static \
    --disable-doxygen \
    --disable-dot \
    --disable-html-docs \
    --disable-latex-docs

# <oden> somehow LIBADD_DL is ignored, is that an intentional change?
perl -pi -e "s|^LIBS =.*|LIBS = -lm -ldl|g" src/cppunit/Makefile

%make

%install
rm -rf %{buildroot}

%makeinstall_std

#(tpg) do not duplicate docs
rm -rf  %{buildroot}%{_datadir}/doc/cppunit

# clean up
rm -rf %{buildroot}%{_datadir}/cppunit
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_libdir}/libcppunit-%{api}.so.%{major}*

%files -n %{develname}
%doc AUTHORS NEWS README THANKS ChangeLog
%{_bindir}/cppunit-config
%{_bindir}/DllPlugInTester
%{_libdir}/*.so
%{_includedir}/cppunit
%{_datadir}/aclocal/cppunit.m4
%{_mandir}/man1/*
%{_libdir}/pkgconfig/cppunit.pc


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.12.1-9mdv2011.0
+ Revision: 661642
- multiarch fixes

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.12.1-8mdv2011.0
+ Revision: 603852
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.12.1-7mdv2010.1
+ Revision: 521117
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.12.1-6mdv2010.0
+ Revision: 413268
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.12.1-5mdv2009.0
+ Revision: 264359
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1.12.1-4mdv2009.0
+ Revision: 212774
- Fix qt3 tool building against gcc 4.3

  + Oden Eriksson <oeriksson@mandriva.com>
    - fix build

* Mon Feb 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.12.1-2mdv2008.1
+ Revision: 174955
- bunzip patch0
- better descriptions
- add full url for source
- fix mixture of tabs and spaces
- use macros
- do not duplicate docs

* Mon Feb 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.1-1mdv2008.1
+ Revision: 174610
- new version
- new major
- update file list

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.12.0-5mdv2008.1
+ Revision: 149130
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1.12.0-4mdv2008.0
+ Revision: 90805
- whoops!

* Tue Sep 18 2007 Oden Eriksson <oeriksson@mandriva.com> 1.12.0-3mdv2008.0
+ Revision: 89517
- new devel naming

* Wed Jul 11 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.0-2mdv2008.0
+ Revision: 51174
- Import cppunit



* Mon Jul 10 2006 Götz Waschk <waschk@mandriva.org> 1.12.0-2mdv2007.0
- fix devel deps

* Sun Jul  2 2006 Götz Waschk <waschk@mandriva.org> 1.12.0-1mdv2007.0
- new major
- New release 1.12.0

* Thu Jun 29 2006 Stefan van der Eijk <stefan@eijk.nu> 1.11.4-3
- rebuild for sparc

* Sat Jun 17 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.11.4-1mdv2007.0
- rebuild for new libpng

* Tue Jan 31 2006 Götz Waschk <waschk@mandriva.org> 1.11.4-1mdk
- split out testrunner
- new major
- update file list
- patch for missing header
- drop patch 0
- New release 1.11.4

* Mon Jan 16 2006 Götz Waschk <waschk@mandriva.org> 1.10.2-6mdk
- fix build

* Sat Jan 07 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.10.2-5mdk
- Rebuild

* Mon Nov 28 2005 Götz Waschk <waschk@mandriva.org> 1.10.2-4mdk
- fix previous change

* Tue Nov 22 2005 Götz Waschk <waschk@mandriva.org> 1.10.2-3mdk
- add qttestrunner

* Tue May  3 2005 Götz Waschk <waschk@mandriva.org> 1.10.2-2mdk
- multiarch support

* Sat Jun 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.10.2-1mdk
- 1.10.2
- fix the funny libname (%%major)

* Sun Nov 02 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.8.0-1mdk
- initial cooker contrib

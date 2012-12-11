
%define plugin	timeline
%define name	vdr-plugin-%plugin
%define version	1.0.141
%define rel	16

Summary:	VDR plugin: Show timer overview and collisions
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.js-home.org/vdr/timeline/
Source:		vdr-%plugin-%version.tar.bz2
Patch0:		91_timeline-1.0.141-1.5.0.dpatch
Patch1:		92_timeline-1.0.141-vdr-1.5.3.dpatch
Patch2:		timeline-1.0.141-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Shows a timeline of all programmed timers per day and informs
you of timer conflicts:
- record transmissions at the same time
and
- transmissions are on different channels (on different frequencies)
and
- there are not enough input devices

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.0.141-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.0.141-15mdv2009.1
+ Revision: 359376
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 1.0.141-14mdv2009.0
+ Revision: 197988
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 1.0.141-13mdv2009.0
+ Revision: 197734
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.5.0 (P0 from e-tobi)
- adapt for api changes of VDR 1.5.3 (P1 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 1.0.141-12mdv2008.1
+ Revision: 145225
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 1.0.141-11mdv2008.1
+ Revision: 103223
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 1.0.141-10mdv2008.0
+ Revision: 50057
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 1.0.141-9mdv2008.0
+ Revision: 42140
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 1.0.141-8mdv2008.0
+ Revision: 22714
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 1.0.141-7mdv2007.0
+ Revision: 90979
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 1.0.141-6mdv2007.1
+ Revision: 74094
- rebuild for new vdr
- Import vdr-plugin-timeline

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 1.0.141-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 1.0.141-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 1.0.141-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 1.0.141-2mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 1.0.141-1mdv2007.0
- 1.0.141
- drop patch1, upstream
- fix description

* Tue Jun 06 2006 Anssi Hannula <anssi@mandriva.org> 0.9.0-1mdv2007.0
- initial Mandriva release


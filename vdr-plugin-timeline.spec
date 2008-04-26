
%define plugin	timeline
%define name	vdr-plugin-%plugin
%define version	1.0.141
%define rel	13

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



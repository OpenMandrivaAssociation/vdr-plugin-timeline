
%define plugin	timeline
%define name	vdr-plugin-%plugin
%define version	1.0.141
%define rel	10

Summary:	VDR plugin: Show timer overview and collisions
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.js-home.org/vdr/timeline/
Source:		vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
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



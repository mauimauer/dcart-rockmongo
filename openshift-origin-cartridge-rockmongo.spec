%global cartridgedir %{_libexecdir}/openshift/cartridges/v2/rockmongo

Summary:   Embedded RockMongo support
Name:      openshift-origin-cartridge-rockmongo
Version: 0.2.1
Release:   1%{?dist}
Group:     Applications/Internet
License:   ASL 2.0 and NBSD
URL:       http://openshift.redhat.com
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires:  openshift-origin-cartridge-mongodb
Requires:  rubygem(openshift-origin-node)

%description
Provides RockMongo V2 cartridge support

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
mkdir -p %{buildroot}/%{_sysconfdir}/openshift/cartridges/v2
cp -r * %{buildroot}%{cartridgedir}/

%post

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}/env
%dir %{cartridgedir}/usr
%dir %{cartridgedir}/etc
%dir %{cartridgedir}/logs
%dir %{cartridgedir}/metadata
%dir %{cartridgedir}/run
%dir %{cartridgedir}/sessions
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE
%doc %{cartridgedir}/README.md

%changelog
* Wed May 08 2013 Adam Miller <admiller@redhat.com> 0.2.1-1
- bump_minor_versions for sprint 28 (admiller@redhat.com)

* Fri May 03 2013 Adam Miller <admiller@redhat.com> 0.1.2-1
- Converted metadata/{locked_files,snapshot*}.txt (fotios@redhat.com)

* Thu Apr 25 2013 Adam Miller <admiller@redhat.com> 0.1.1-1
- Split v2 configure into configure/post-configure (ironcladlou@gmail.com)
- implementing install and post-install (dmcphers@redhat.com)
- Bug 954110 - Share RockMongo source across gear instances (jhonce@redhat.com)
- bump_minor_versions for sprint XX (tdawson@redhat.com)

* Mon Apr 15 2013 Adam Miller <admiller@redhat.com> 0.0.7-1
- WIP Cartridge Refactor - Scrub manifests (jhonce@redhat.com)

* Wed Apr 10 2013 Adam Miller <admiller@redhat.com> 0.0.6-1
- WIP Cartridge Refactor - Fix ERB env variables (jhonce@redhat.com)

* Tue Apr 09 2013 Adam Miller <admiller@redhat.com> 0.0.5-1
- message improvement (dmcphers@redhat.com)

* Mon Apr 08 2013 Dan McPherson <dmcphers@redhat.com> 0.0.4-1
- new package built with tito

* Mon Apr 08 2013 Jhon Honce <jhonce@redhat.com> 0.0.3-1
- WIP Cartridge Refactor - RockMongo cartridge (jhonce@redhat.com)
- Automatic commit of package [openshift-origin-cartridge-rockmongo] release
  [0.0.2-1]. (jhonce@redhat.com)
- WIP Cartridge Refactor - RockMongo cartridge (jhonce@redhat.com)

* Thu Apr 04 2013 Jhon Honce <jhonce@redhat.com> 0.0.2-1
- new package built with tito



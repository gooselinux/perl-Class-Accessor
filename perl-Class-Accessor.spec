Name:           perl-Class-Accessor
Version:        0.31
Release:        6.1%{?dist}
Summary:        Automated accessor generation
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Class-Accessor/
Source0:        http://search.cpan.org/CPAN/authors/id/K/KA/KASEI/Class-Accessor-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.1, perl(Test::More)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
%{summary}.

%prep
%setup -q -n Class-Accessor-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make 

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes examples/
%{perl_vendorlib}/Class
%{_mandir}/man3/*.3*


%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 0.31-6.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-4
- Rebuild for perl 5.10 (again)

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.31-3
- rebuild for new perl

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.31-2
- license fix

* Fri Jul 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.31-1
- update for 0.31, hooray for performance patches

* Wed Jan 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.30-1
- bump to 0.30

* Thu Sep 14 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.27-2
- bump for fc6

* Wed Aug  2 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.27-1
- bump to 0.27

* Fri Mar 31 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.25-1
- bump to 0.25

* Mon Jan  9 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.22-1
- bump to 0.22

* Fri Aug  5 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.19-3
- add examples/ to %doc

* Fri Jul  8 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.19-2
- cleanups

* Wed Jul  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.19-1
- Initial package for Fedora Extras

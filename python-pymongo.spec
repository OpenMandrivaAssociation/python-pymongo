%define shortname    pymongo

Name:           python-%{shortname}
Version:        2.5.2
Release:        1
Summary:        Python driver for MongoDB
Group:          Development/Python
License:        Apache License
URL:            http://api.mongodb.org/python/2.1/
Source0:        http://pypi.python.org/packages/source/p/pymongo/pymongo-%{version}.tar.gz
BuildRequires:  python-setuptools
%py_requires -d

%define debug_package %{nil}

%description
The PyMongo distribution contains tools for interacting with MongoDB
database from Python.

The bson package is an implementation of the BSON format for Python.
The pymongo package is a native Python driver for MongoDB.
The gridfs package is a gridfs implementation on top of pymongo.
This driver is build without the C extensions.

%prep
%setup -q -n %{shortname}-%{version}

%build
%{__python} setup.py --no_ext build

%install
%{__python} setup.py --no_ext install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir

%files
%{py_platsitedir}/*


%changelog
* Fri May 11 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.2-1
+ Revision: 798307
- version update 2.2

* Thu Jan 05 2012 Lev Givon <lev@mandriva.org> 2.1.1-1
+ Revision: 757840
- Update to 2.1.1.

* Wed Dec 07 2011 Lev Givon <lev@mandriva.org> 2.1-1
+ Revision: 738759
- Update to 2.1.

* Wed Oct 26 2011 Lev Givon <lev@mandriva.org> 2.0.1-1
+ Revision: 707359
- Update to 2.0.1.

* Thu Jun 09 2011 Alexandre Lissy <alissy@mandriva.com> 1.11-1
+ Revision: 683426
- Updating python-pymongo to latest 1.11 (ipv6 support!)

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.1-1
+ Revision: 662538
- update to new version 1.10.1

* Wed Dec 08 2010 Wiliam Alves de Souza <wiliam@mandriva.com> 1.9-1mdv2011.0
+ Revision: 616254
- import python-pymongo




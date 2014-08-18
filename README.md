# grunt-optimizer-cleanup

This repository contains a [Grunt](http://gruntjs.com) project to automate the deletion of files and folders from the Esri ArcGIS API for JavaScript [Web Optimizer](http://jso.arcgis.com).  It is important to not just blindly run this, but to understand what files are being deleted.

You will need to first use the [ArcGIS API for JavaScript Web Optimizer](http://jso.arcgis.com/) to create an optimized build of the *ArcGIS API for JavaScript* based upon your application source code. For more information see the [ArcGIS API for JavaScript Web Optimizer](http://jso.arcgis.com/help/) help. This project runs Grunt tasks to create a copy of your custom build, then delete files that the Web Optimizer currently leaves behind just in case you application would need them.

**Overview of what this project will do**:

1. Download and unzip your build into the ```library-before``` folder (**you must do this manually**).
2. Delete the ```dijit``` and ```dojox``` folders.
3. Inside the ```esri``` folder, delete the ```toolbars``` folder.
4. Inside ```esri/dijit```, delete everything except the ```images``` folder.
5. Specify which locales to delete under the ```dojo/nls``` directory
6. The ```library-after``` folder will contain the ```minimized``` API.

## Licensing
Copyright 2014 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's [license.txt](license.txt) file.
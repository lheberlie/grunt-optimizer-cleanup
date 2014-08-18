(function () {
    "use strict";
}());

module.exports = function (grunt) {
    // show elapsed time at the end
    require("time-grunt")(grunt);
    // load all grunt tasks
    require("load-grunt-tasks")(grunt);

    grunt.initConfig(
        {
            pkg: grunt.file.readJSON("package.json"),
            // ---------------------------------------------------------------------
            // grunt-contrib-copy
            // ---------------------------------------------------------------------
            copy: {
                duplicate_api: {
                    files: [
                        { expand: true,
                            cwd: "<%= pkg.api_dir_before %>",
                            src: ["**/*"], dest: "<%= pkg.api_dir_after %>/"
                        }
                    ]
                }
            },
            // ---------------------------------------------------------------------
            // grunt-contrib-clean
            // ---------------------------------------------------------------------
            clean: {
                library_after: {
                    src: ["library-after"]
                },
                dijit_dojox_extras: [
                    "<%= pkg.api_dir_after %>/dijit",
                    "<%= pkg.api_dir_after %>/dojox",
                    // ---------------------------------------------
                    // Clean up any custom package folders
                    // ---------------------------------------------
                    "<%= pkg.api_dir_after %>/extras"
                ],
                esri_toolbars: [
                    "<%= pkg.api_dir_after %>/esri/toolbars"
                ],
                esri_dijit: {
                    src: [

                        "<%= pkg.api_dir_after %>/esri/dijit/*",
                        // ---------------------------------------------
                        // Keep the esri/dijit/images folder
                        // ---------------------------------------------
                        "!<%= pkg.api_dir_after %>/esri/dijit/images/**"
                    ]
                },
                nls: {
                    src: [
                        // ---------------------------------------------
                        // Delete everything in the dojo/nls folder
                        // ---------------------------------------------
                        "<%= pkg.api_dir_after %>/dojo/nls/*",
                        // ---------------------------------------------
                        // Keep the files listed below
                        // ---------------------------------------------
                        "!<%= pkg.api_dir_after %>/dojo/nls/dojo_ROOT.js",
                        "!<%= pkg.api_dir_after %>/dojo/nls/dojo_ja-jp.js"
                    ]
                }
            },
            // ---------------------------------------------------------------------
            //
            // ---------------------------------------------------------------------
            size_report: {
                before: {
                    files: {
                        list: ["<%= pkg.api_dir_before %>/**/*"]
                    }
                },
                after: {
                    files: {
                        list: ["<%= pkg.api_dir_after %>/**/*"]
                    }
                }
            }
        }
    )
    ;

    grunt.registerTask("default", [
        "clean:library_after",
        "copy",
        "clean:dijit_dojox_extras",
        "clean:esri_toolbars",
        "clean:esri_dijit",
        "clean:nls",
        "size_report"
    ]);
}
;
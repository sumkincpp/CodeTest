Package.ManifestAttributes((
          "Class-Path", classpath.files
            .map(f => f.getName)
            .filter(_.endsWith(".jar"))
            .mkString(" ")))}

artifactName in Compile := { (_, _, artifact: Artifact) => artifact.name + "." + artifact.extension }

artifactName in Test := { (_, _, artifact: Artifact) => artifact.name + "-test." + artifact.extension }

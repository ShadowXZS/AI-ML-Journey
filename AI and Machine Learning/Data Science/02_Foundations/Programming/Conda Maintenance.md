| **Task**                                  | **Command**                                                                                       |     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------- | --- |
| **Check Environment Health**              | `conda list`                                                                                      |     |
| **Sync Environment with YAML**            | `conda env update --file environment.yml --prune`                                                 |     |
| **Add a New "Tool"**                      | `conda install <package>` followed by `conda env export > environment.yml`                        |     |
| **Nuclear Option** (If everything breaks) | `conda deactivate`, `conda env remove -n aiandml_env`, then `conda env create -f environment.yml` |     |
| Cross Reference                           | conda compare environment.yml                                                                     |     |

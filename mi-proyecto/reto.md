# Diferencia entre `git merge` y `git rebase`

Cuando trabajamos con Git y tenemos ramas paralelas, existen diferentes formas de integrar los cambios. Las dos más comunes son **merge** y **rebase**, y aunque ambas logran el objetivo de unificar el trabajo, lo hacen de manera distinta.

---

## git merge
`git merge` combina los cambios de una rama en otra creando un **commit de merge** adicional.  
Esto mantiene intacto el historial de ambas ramas, mostrando las bifurcaciones y cuándo se unieron.

**Ejemplo:**
```bash
# Nos ubicamos en la rama principal
git checkout main

# Unimos los cambios de la rama feature
git merge feature

########

##  git rebase

`git rebase` toma los commits de una rama y los reaplica sobre otra base, reescribiendo el historial para que parezca que esos cambios se hicieron directamente desde la rama base.  
A diferencia de `merge`, no se crea un commit extra, sino que se reorganiza la secuencia de commits para mantener un historial lineal.

**Ejemplo:**
```bash
# Nos ubicamos en la rama feature
git checkout feature

# Reaplicamos nuestros commits sobre la rama principal
git rebase main


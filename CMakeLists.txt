cmake_minimum_required(VERSION 3.22)

# Définir le nom du projet
project(CalculSomMinMax VERSION 1.0)

set(CMAKE_C_STANDARD 23)
set(CMAKE_C_STANDARD_REQUIRED True)

set(SOURCES IntTable.c)
set(HEADERS IntTable.h)
set(EXECUTABLE_NAME ${PROJECT_NAME}App)
set(LIBRARY_NAME ${PROJECT_NAME}Lib)

# Créer l'executable à partir du code source
add_executable(${EXECUTABLE_NAME} ${SOURCES})


# Créer une bibliothèque partagée à partir du code source
add_library(${LIBRARY_NAME} SHARED ${SOURCES})


# Définir les propriétés de la bibliothèque
set_target_properties(${LIBRARY_NAME} PROPERTIES
        PUBLIC_HEADER ${HEADERS}
        VERSION 1.0.0
        SOVERSION 1
)

# Inclure les répertoires si nécessaire
# include_directories(chemin_vers_les_en-têtes)

# Spécifier l'installation de la bibliothèque (optionnel)
install(TARGETS ${LIBRARY_NAME}
        LIBRARY DESTINATION lib
        PUBLIC_HEADER DESTINATION include
)

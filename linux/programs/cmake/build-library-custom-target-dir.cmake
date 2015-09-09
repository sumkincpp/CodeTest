# Target library custom build location
# https://stackoverflow.com/questions/2814126/cmake-add-library-at-a-custom-location

ADD_LIBRARY(example MODULE example.c)

# Proper way

set_target_properties(example PROPERTIES 
  LIBRARY_OUTPUT_DIRECTORY "${CUSTOM_OUTDIR}"
)
# i.e. 
set_target_properties(example PROPERTIES 
  LIBRARY_OUTPUT_DIRECTORY lib
)

# Not that great way

GET_TARGET_PROPERTY(FILEPATH example LOCATION)
ADD_CUSTOM_COMMAND(
    TARGET example POST_BUILD 
    COMMAND ${CMAKE_COMMAND} 
    ARGS -E copy ${FILEPATH} ${CUSTOM_OUTDIR}
)

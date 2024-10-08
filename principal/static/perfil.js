// Función para cambiar entre editar y guardar
function toggleEdit(campoId, botonId) {
    const campo = document.getElementById(campoId);
    const boton = document.getElementById(botonId);

    if (boton.innerText === 'Editar') {
        // Cambiar de modo visualización (span) a modo edición (input)
        const valorActual = campo.innerText;
        const nuevoInput = document.createElement('input');
        nuevoInput.type = (campoId === 'correoElectronico') ? 'email' : 'text';
        nuevoInput.value = valorActual;
        nuevoInput.id = campoId; // Asigna un ID al input (si lo necesitas)
        
        campo.replaceWith(nuevoInput);
        boton.innerText = 'Guardar'; // Cambiar el botón a "Guardar"
    } else {
        // Cambiar de modo edición (input) a modo visualización (span)
        const nuevoValor = campo.value;
        const nuevoSpan = document.createElement('span');
        nuevoSpan.innerText = nuevoValor;
        nuevoSpan.id = campoId; // Mantén el mismo id para el span
        campo.replaceWith(nuevoSpan);
        boton.innerText = 'Editar'; // Cambiar el botón a "Editar"
    }
}

// Asignar los eventos a los botones con la misma lógica
document.getElementById('editar-nombre').addEventListener('click', function () {
    toggleEdit('nombreCompleto', 'editar-nombre');
});

document.getElementById('editar-celular').addEventListener('click', function () {
    toggleEdit('numeroCelular', 'editar-celular');
});

document.getElementById('editar-correo').addEventListener('click', function () {
    toggleEdit('correoElectronico', 'editar-correo');
});

// Función para seleccionar imagen
document.getElementById('editar-imagen').addEventListener('click', function() {
    document.getElementById('imagenPerfil').click(); // Simula el clic en el input de archivo
});

// Manejar el evento change para mostrar una vista previa de la imagen seleccionada
document.getElementById('imagenPerfil').addEventListener('change', function(event) {
    const file = event.target.files[0]; // Obtiene el archivo seleccionado
    if (file) {
        const reader = new FileReader(); // Crea un nuevo objeto FileReader
        reader.onload = function(e) {
            const preview = document.getElementById('preview'); // Encuentra el elemento de vista previa
            preview.src = e.target.result; // Asigna el resultado a la imagen de vista previa
            preview.style.display = 'block'; // Muestra la imagen
        };
        reader.readAsDataURL(file); // Lee el archivo como una URL de datos
    }
});

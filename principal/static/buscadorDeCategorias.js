// Seleccionar todos los botones de categorías y subcategorías
const buttons = document.querySelectorAll('.custom-btn');

// Seleccionar el contenedor de productos
const productsGrid = document.getElementById('products');

// Función para filtrar productos según la categoría y subcategoría
function filterProducts(category, subcategory) {
    const products = document.querySelectorAll('.product-card');
    
    // Recorrer todos los productos y mostrar u ocultar según la categoría y subcategoría
    products.forEach(product => {
        const productCategory = product.getAttribute('data-category');
        const productSubcategory = product.getAttribute('data-subcategory');
        const productH4 = product.querySelector('h4'); // Seleccionamos el h4 del producto
        
        // Si el contenido de h4 coincide con la subcategoría, mostramos el producto
        if (productH4 && productH4.textContent === subcategory) {
            product.style.display = 'block'; // Mostrar el producto si el h4 es igual a subcategory
        } 
        // Si la categoría y subcategoría no coinciden con las seleccionadas, ocultamos el producto
        else if (productCategory === category && productSubcategory === subcategory) {
            product.style.display = 'block'; // Mostrar el producto si coincide
        } else {
            product.style.display = 'none'; // Ocultar si no coincide
        }
    });
}

// Agregar evento de click a cada botón para filtrar productos
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const category = button.getAttribute('data-category');
        const subcategory = button.getAttribute('data-subcategory');
        filterProducts(category, subcategory);
    });
});
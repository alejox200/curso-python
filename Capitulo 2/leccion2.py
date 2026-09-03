#Datos iniciales
rol = input("Ingresa tu rol en el sistema (admin/editor/invitado): ").strip().lower()

#Procesamiento
if rol == "admin":
    print("🔑 Aceso Total: Puedes crear, editar y eliminar bases de datso.")
elif rol == "editor":
    print("📝 Aceso Medio: Puedes crear y modificar contenido, pero no borrar usuarios.")
elif rol == "invitado":
    print("👀 Aceso de Lectura: Solo puedes ver los reportes.")
else:
    print("❌ Rol desconocido: No tienes permiso para acceder al sistema.")
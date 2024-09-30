Add-Type -AssemblyName PresentationFramework

# Crear la ventana en pantalla completa sin bordes
$Window = New-Object System.Windows.Window
$Window.Title = "Windows Update"
$Window.WindowStyle = 'None'  # Sin bordes
$Window.ResizeMode = 'NoResize'
$Window.Background = "#0078d7"  # Color similar a las actualizaciones de Windows
$Window.Topmost = $true  # Mantener la ventana encima de las demás
$Window.WindowStartupLocation = 'CenterScreen'
$Window.Cursor = [System.Windows.Input.Cursors]::Wait  # Cambiar el cursor al símbolo de carga

# Configurar para pantalla completa
$Window.WindowState = 'Maximized'

# Crear el contenedor de texto principal con dos líneas
$TextBlock = New-Object System.Windows.Controls.TextBlock
$TextBlock.FontSize = 40
$TextBlock.Foreground = "White"
$TextBlock.HorizontalAlignment = "Center"
$TextBlock.VerticalAlignment = "Center"
$TextBlock.TextAlignment = "Center"
$TextBlock.Margin = "0, 0, 0, 50"  # Margen inferior para ajustar el texto en pantalla

# Añadir el texto con salto de línea utilizando LineBreak
$Run1 = New-Object System.Windows.Documents.Run("Updating Windows")
$LineBreak = New-Object System.Windows.Documents.LineBreak
$Run2 = New-Object System.Windows.Documents.Run("Please do not turn off your computer.")

# Añadir los objetos al TextBlock
$TextBlock.Inlines.Add($Run1)
$TextBlock.Inlines.Add($LineBreak)
$TextBlock.Inlines.Add($Run2)

# Crear un StackPanel para agrupar los elementos
$StackPanel = New-Object System.Windows.Controls.StackPanel
$StackPanel.HorizontalAlignment = "Center"
$StackPanel.VerticalAlignment = "Center"
$StackPanel.Children.Add($TextBlock)

# Asignar el StackPanel al contenido de la ventana
$Window.Content = $StackPanel

# Mostrar la ventana
$Window.Show()

# Temporizador para cerrar la ventana después de 20 segundos
Start-Sleep -Seconds 20

# Cerrar la ventana automáticamente
$Window.Close()

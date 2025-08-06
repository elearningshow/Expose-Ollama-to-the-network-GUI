"# Expose-Ollama-to-the-network-GUI"  

Where to enable the Expose Ollama to the network setting (Make sure to enable this feature)
<div align="center">
  <img alt="Expose-Ollama-to-the-network-GUI" height="200px" src="https://github.com/elearningshow/Expose-Ollama-to-the-network-GUI/blob/main/ollama_on_lan.jpg">
</div>

What the Ollama GUI will look like to those on your LAN or those outside local lan with router configuration
<div align="center">
  <img alt="Expose-Ollama-to-the-network-GUI" height="200px" src="https://github.com/elearningshow/Expose-Ollama-to-the-network-GUI/blob/main/ollama_gui_lan.jpg">
</div>

What to do in order to make the server accessible via the internet not just the lan (You can setup your router to enable port forwarding internal port would be 5000 and external port would be 5001.  You would connect to your external ip number (my_external_ip:5001) that would have the router connect to your (internal_ip_server:5000) and enjoy. )
<div align="center">
  <img alt="Expose-Ollama-to-the-network-GUI" height="200px" src="https://github.com/elearningshow/Expose-Ollama-to-the-network-GUI/blob/main/port_forward_main_pc.jpg">
</div>

and then run the startserver-ask.bat it will open the GUI and now everyone on your LAN can enjoy a Ollama GUI.










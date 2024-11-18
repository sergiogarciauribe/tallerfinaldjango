from abc import ABC, abstractmethod 
 
class IPagable(ABC): 
 @abstractmethod 
 def pagar(self, metodo_pago: str) -> bool: pass
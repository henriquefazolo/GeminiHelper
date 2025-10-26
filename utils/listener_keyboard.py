# utils.listener_keyboard
from utils.logger import Logger
import keyboard
import logging
import asyncio
from typing import Dict, Optional, Callable
from datetime import datetime


class ListenerKeyboard:
    def __init__(self):
        self.callbacks: Dict[str, Callable] = {}
        self.status: Optional[bool] = None
        self.logger = Logger(name=f'{__name__}.{self.__class__.__name__}')

    async def start(self):
        try:
            self.logger.info('Started ListenerKeyboard')
            self.status = True
            keyboard.on_press(self.execute)
        except Exception as e:
            self.logger.exception(e)

    def execute(self, event):
        try:
            if not self.status:
                self.logger.warning('Key event received but listener is inactive')
                return
            key_name = event.name

            if key_name in self.callbacks:
                self.logger.info(f"Executing callback for key: '{key_name}'")
                try:
                    callback = self.callbacks[key_name]
                    if asyncio.iscoroutinefunction(callback):
                        # Para callbacks assíncronos
                        loop = asyncio.get_event_loop()
                        loop.create_task(callback(event))
                    else:
                        # Para callbacks síncronos
                        callback(event)
                except Exception as e:
                    self.logger.error(f"Error in callback for key '{key_name}': {e}")
        except Exception as e:
            self.logger.exception(e)

    def stop(self):
        try:
            self.logger.info('Stoping ListenerKeyboard')
            if self.status:
                keyboard.unhook_all()
                self.status = False
            else:
                logging.warning('Listener was already stopped')

        except Exception as e:
            self.logger.exception(e)

    def add_callback(self, key_name: str, callback: Callable):
        try:
            self.callbacks[key_name] = callback
            self.logger.info(f"Callback added for key: '{key_name}'")
        except Exception as e:
            self.logger.exception(f"Error adding callback for '{key_name}': {str(e)}")


if __name__ == '__main__':
    async def run():
        listener = ListenerKeyboard()

        try:
            def callback_esc(event):
                print(event)

            listener.add_callback('esc', callback_esc)

            await listener.start()
            await asyncio.sleep(10)
        except KeyboardInterrupt:
            print("Interrupção do usuário detectada")
        finally:
            listener.stop()


    asyncio.run(run())


import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from db.storage import UserStorage, User

class TG_Bot():
    def __init__(self, tg_api_key: str, user_storage: UserStorage):
        self._user_storage:UserStorage = user_storage
        self._bot:aiogram.Bot = aiogram.Bot(token=tg_api_key)
        self._storage:MemoryStorage = MemoryStorage()
        self._dispatcher:aiogram.Dispatcher = aiogram.Dispatcher(self._bot, storage=self._storage)
        self._disable_web_page:bool = True
        self._accounts_in_process_pool = {}
        self._create_keyboards()

    async def init(self) :
        self._init_handler()

    async def start(self):
        print('Bot has started')
        await self._dispatcher.start_polling()

    def _init_handler(self) :
        self._dispatcher.register_message_handler(self._user_middleware(self._cmd_start), commands=['start'])

    async def _cmd_start(self, message:aiogram.types.Message , user:User):
        await message.answer('Меню')
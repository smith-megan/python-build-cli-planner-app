from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from abc import ABC

class DeadlinedMetaReminder(Iterable, ABCMeta):
  @abstractmethod
  def is_due(self):
    pass
  def __iter__(Iterable):
    pass

class DeadlinedReminder(Iterable, ABC):
  @abstractmethod
  def is_due(self):
    pass
  def __iter__(Iterable):
    pass

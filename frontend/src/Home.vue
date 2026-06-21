<template>
  <el-alert title="感谢计时器生成器交流群的群友们热心提供存档，协助开发。代码仓库：https://github.com/CuteReimu/ss-completion" type="info" effect="dark" close-text="前往" @close="openGithub"></el-alert>
  <el-upload drag accept=".dat" :auto-upload="false" :show-file-list="false" :on-change="onUploadFile">
    <el-icon class="el-icon--upload"><upload-filled style="width: 80px;"></upload-filled></el-icon>
    <div class="el-upload__text">
      你可以将存档文件拖拽到这里或者 <em>点击上传</em>
    </div>
  </el-upload>
  <div class="btn-container">
    <el-button @click="refreshUserDataFiles" type="primary">刷新列表</el-button>
    <el-select
      v-model="selectedUserDataFile"
      :options="userDataFiles"
      style="max-width: 220px"
      placeholder="选择本地存档"
      @change="selectUserData"
    ></el-select>
    <el-button
      style="margin-right: 15px"
      type="primary"
      @click="selectUserData"
      :disabled="selectedUserDataFile===''"
    ><el-icon><RefreshRight /></el-icon></el-button>
    <el-button @click="OpenDataFolder" type="primary">打开存档目录</el-button>
    <el-button @click="OutputResult" type="primary" :disabled="disableReloadBtn">将解析后的存档导出为json</el-button>
    <el-button @click="ModifyAnalyzeScript" type="danger">修改解析脚本</el-button>
    <el-button @click="RefreshAnalyze" type="danger" :disabled="disableReloadBtn">重新加载解析脚本</el-button>
  </div>
  <el-text size="large" style="margin: 10px 0;">完成度：{{data.Completion ?? 0}}%</el-text>
  <div class="card-container">
    <el-card v-for="category in data.Categories">
      <template #header>{{category.name}}</template>
      <el-table :show-header="false" border :data="category.items" :row-class-name="determineRowClass" @row-click="goToWiki">
        <el-table-column label="名称">
          <template #default="scope">
            <el-tooltip effect="dark" v-if="scope.row.desc" :content="scope.row.desc" placement="left">
              <div><el-image v-if="scope.row.icon" :src="scope.row.icon" fit="scale-down" />{{scope.row.show_text}}</div>
            </el-tooltip>
            <div v-else><el-image v-if="scope.row.icon" :src="scope.row.icon" fit="scale-down" />{{scope.row.show_text}}</div>
          </template>
        </el-table-column>
        <el-table-column prop="status_text" label="状态" width="80">
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import {
  ElAlert, ElText, ElUpload, ElIcon, ElTable, ElTableColumn, ElSelect,
  ElButton, UploadFile, ElMessage, ElCard, ElTooltip, ElImage,
} from 'element-plus';
import { RefreshRight, UploadFilled } from '@element-plus/icons-vue';
import { BrowserOpenURL, LogError } from '../wailsjs/runtime';
import { OpenDataFolder, DecryptFile, ReDecryptFile, SaveBuf, ModifyScript, ShowDataFolder, SelectUserData } from '../wailsjs/go/main/App';
import { main } from "../wailsjs/go/models";

interface OptionData {
  label: string
  value: string
}

const disableReloadBtn = ref(true);
const data = ref<main.AnalyzeResult>(new main.AnalyzeResult());
const selectedUserDataFile = ref("");
const userDataFiles = ref<OptionData[]>([]);

const refreshUserDataFiles = () => {
  ShowDataFolder().then(files => {
    userDataFiles.value = files.map(v => ({label: v, value: v}));
  });
};

const selectUserData = () => {
  SelectUserData(selectedUserDataFile.value).then(res => {
    data.value = res;
    disableReloadBtn.value = false;
    ElMessage({ message: "解析成功", type: 'success', plain: true });
  }).catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  });
};

function determineRowClass({row}) {
  let c = '';
  switch (row.status) {
    case 2: c = 'success-row'; break;
    case 1: c = 'warning-row'; break;
    default: c = 'danger-row'; break;
  }
  if (row.wiki) c += " clickable-row";
  return c;
}

function onUploadFile(file: UploadFile) {
  if (!file?.raw) return;
  file.raw.text().then(text => {
    DecryptFile(text).then(res => {
      data.value = res;
      disableReloadBtn.value = false;
      ElMessage({ message: "解析成功", type: 'success', plain: true });
    }).catch(err => {
      LogError(err);
      ElMessage({ message: String(err), type: 'error', plain: true });
    })
  }).catch(e => {
    LogError(e);
    ElMessage({ message: String(e), type: 'error', plain: true });
  });
}

function RefreshAnalyze() {
  ReDecryptFile().then(res => {
    data.value = res;
    ElMessage({ message: "解析成功", type: 'success', plain: true });
  }).catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  })
}

function OutputResult() {
  SaveBuf().catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  })
}

function ModifyAnalyzeScript() {
  ModifyScript().catch(err => {
    LogError(err);
    ElMessage({ message: String(err), type: 'error', plain: true });
  })
}

function openGithub() {
  BrowserOpenURL('https://github.com/CuteReimu/ss-completion');
}

function goToWiki(row: main.ItemResult) {
  if (row.wiki) BrowserOpenURL(row.wiki);
}

onMounted(() => {
  refreshUserDataFiles();
});
</script>
